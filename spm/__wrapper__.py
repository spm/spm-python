import warnings
import numpy as np
from functools import partial
from collections.abc import (
    MutableSequence, MutableMapping, KeysView, ValuesView, ItemsView
)

# If scipy is available, convert matlab sparse matrices scipy.sparse
# otherwise, convert them to dense numpy arrays
try:
    from scipy import sparse
except (ImportError, ModuleNotFoundError):
    sparse = None

# We'll complain later if the runtime is not instantiated
matlab = None


def _import_matlab():
    global matlab
    if matlab is None:
        try:
            import matlab
        except (ImportError, ModuleNotFoundError):
            ...


# ----------------------------------------------------------------------
# Questions
# ----------------------------------------------------------------------

"""
* MATLAB does not have 1D arrays (they are always 2D).
  A 1D python array is interpreted as a row arrays, so the round trip
  goes [1, 2, 3] -> [[1, 2, 3]].
  Are we happy with that? I think it works in the sense that
  when a numpy operation takes a matrix and a vector, the vector is
  broadcasted to its left, and is therefore interpreted as a row vector.

  !! We should clearly document this behaviour.

* The creation of numeric vectors on the python side is currently
  quite verbose (`Array.from_any([0, 0])`, because `Array([0, 0])`
  is interpreted as "create an empty array with shape [0, 0]").
  We could either
  - introduce a concise helper (e.g., `num`) to make this less verbose:
    `Array.from_any([0, 0])` -> `num([0, 0])`
  - Interpret lists of numbers as Arrays rather than Cells. But this is
    problematic when parsing the output of a mpython_endpoint call, since
    lists of numbers do mean "cell" in this context.

* I've added support for "object arrays" (such as nifti or cfg_dep)
  in DelayedArray:
  > `a.b[0] = nifti("path")` means that `a.b` contains a 1x1 nifti object.
  However, I only support 1x1 object, and the index must be 0 or -1.
  There might be a way to make this more generic, but it needs more thinking.
  The 1x1 case is all we need for batch jobs (it's required when building
  jobs with dependencies).

  It might be useful to have a `ObjectArray` type (with `MatlabClass`
  as a base class?) for such objects -- It'll help with the logic in
  delayed arrays. It should be detectable by looking for `class(struct(...))`
  in the constructor when parsing the matlab code, although there are
  cases where the struct is created beforehand, e.g.:
  https://github.com/spm/spm/blob/main/%40nifti/nifti.m#L12

  Maybe there's a programmatic way in matlab to detect if a class is
  a pure object or an object array? It seems that old-school classes
  that use the class(struct) constructor are always object arrays.
  With new-style classes, object arrays can be constructed after the
  fact:
  https://uk.mathworks.com/help/matlab/matlab_oop/creating-object-arrays.html

  After more thinking, it also means that we have again a difference in bhv
  between `x{1} = object` and `x(1) = object`. In the former case, x is
  a cell that contains an object, whereas in the latter x is a 1x1 object
  array.

* We should probably implement a helper to convert matlab batches into
  python batches.
"""

# ----------------------------------------------------------------------
# Runtime
# ----------------------------------------------------------------------


class Runtime:
    """Namespace that holds the matlab runtime. All methods are static."""

    _initialize = None
    _instance = None
    verbose = True

    @staticmethod
    def instance():
        if Runtime._instance is None:
            if Runtime.verbose:
                print('Initializing Matlab Runtime...')
            Runtime._import_initialize()
            Runtime._instance = Runtime._initialize()
        return Runtime._instance

    @staticmethod
    def call(fn, *args, **kwargs):
        (args, kwargs) = Runtime._process_argin(*args, **kwargs)
        res = Runtime.instance().mpython_endpoint(fn, *args, **kwargs)
        return Runtime._process_argout(res)

    @staticmethod
    def _process_argin(*args, **kwargs):
        to_runtime = MatlabType._to_runtime
        args = tuple(map(to_runtime, args))
        kwargs = dict(zip(kwargs.keys(), map(to_runtime, kwargs.values())))
        return args, kwargs

    @staticmethod
    def _process_argout(res):
        return MatlabType.from_any(res)

    @staticmethod
    def _import_initialize():
        # NOTE(YB)
        #   I moved the import within a function so that array wrappers
        #   can be imported and used even when matlab is not properly setup.
        if Runtime._initialize:
            return
        try:
            from spm._spm import initialize
            Runtime._initialize = initialize
        except ImportError as e:
            # ~~~ UNUSED ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # import os
            # installer_path = os.path.join(
            #     os.path.dirname(os.path.abspath(__file__)),
            #     '_spm',
            #     'resources',
            #     'RuntimeInstaller.install'
            # )
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            print(Runtime._help)
            raise e
        # Make sure matlab is imported
        _import_matlab()

    _help = """
    Failed to import spm._spm. This can be due to a failure to find Matlab
    Runtime. Please verify that Matlab Runtime is installed and its path is set.
    See https://www.mathworks.com/help/compiler/mcr-path-settings-for-run-time-deployment.html
    for instructions on how to setup the path.
    If the issue persists, please open an issue with the entire error
    message at https://github.com/spm/spm-python/issues.
    """


# ----------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------


def _copy_if_needed(out, inp, copy=None) -> np.ndarray:
    """Fallback implementation for asarray(*, copy: bool)"""
    if (
        out is not None and
        isinstance(inp, np.ndarray) and
        np.ndarray.view(out, np.ndarray).data !=
        np.ndarray.view(inp, np.ndarray).data
    ):
        if copy:
            out = np.copy(out)
        elif copy is False:
            raise ValueError("Cannot avoid a copy")
    return out


def _spcopy_if_needed(out, inp, copy=None):
    """Fallback implementation for asarray(*, copy: bool)"""
    if (
        out is not None and
        isinstance(inp, sparse.sparray) and
        out.data.data != inp.data.data
    ):
        if copy:
            out = out.copy()
        elif copy is False:
            raise ValueError("Cannot avoid a copy")
    return out


def _matlab_array_types():
    """Return a mapping from matlab array type to numpy data dtype."""
    _import_matlab()
    global matlab
    if matlab:
        return {
            matlab.double:  np.float64,
            matlab.single:  np.float32,
            matlab.logical: np.bool,
            matlab.uint64:  np.uint64,
            matlab.uint32:  np.uint64,
            matlab.uint16:  np.uint16,
            matlab.uint8:   np.uint8,
            matlab.int64:   np.int64,
            matlab.int32:   np.int32,
            matlab.int16:   np.int16,
            matlab.int8:    np.int8,
        }
    else:
        return {}


def _empty_array() -> "Array":
    """Matlab's default cell/struct elements are 0x0 arrays."""
    return Array.from_shape([0, 0])


# ----------------------------------------------------------------------
# Types
# ----------------------------------------------------------------------


class MatlabType(object):
    """Generic type for objects that have an exact matlab equivalent."""

    @classmethod
    def from_any(cls, other, **kwargs):
        """
        Convert python/matlab objects to `MatlabType` objects
        (`Cell`, `Struct`, `Array`, `MatlabClass`).

        !!! warning "Conversion is performed in-place when possible."
        """
        # - we do not convert to matlab's own array types
        #   (`matlab.double`, etc);
        # - we do not convert to types that can be passed directly to
        #   the matlab runtime;
        # - instead, we convert to python types that mimic matlab types.
        _from_any = partial(cls.from_any, **kwargs)
        _from_runtime = kwargs.pop("_from_runtime", False)

        if isinstance(other, MatlabType):
            if isinstance(other, AnyDelayedArray):
                other._error_is_not_finalized()
            return other

        if isinstance(other, dict):
            if "type__" in other:
                type__ = other["type__"]

                if type__ == "structarray":
                    # MPython returns a list of dictionaries in data__
                    # and the array shape in size__.
                    return Struct._from_runtime(other)

                elif type__ == "cell":
                    # MPython returns a list of dictionaries in data__
                    # and the array shape in size__.
                    return Cell._from_runtime(other)

                elif type__ == "object":
                    # MPython returns the object's fields serialized
                    # in a dictionary.
                    return MatlabClass._from_runtime(other)

                elif type__ == "sparse":
                    # MPython returns the coordinates and values in a dict.
                    return SparseArray._from_runtime(other)

                elif type__ == "char":
                    # Character array that is not a row vector
                    # (row vector are converted to str automatically)
                    # MPython returns all rows in a (F-ordered) cell in data__
                    # Let's use the cell constructor to return a cellstr.
                    # -> A cellstr is a column vector, not a row vector
                    size = np.asarray(other["size__"]).tolist()[0]
                    size = size[:-1] + [1]
                    other["type__"] = "cell"
                    other["size__"] = np.asarray([size])
                    return Cell._from_runtime(other)

                else:
                    raise ValueError("Don't know what to do with type", type__)

            else:
                other = type(other)(
                    zip(other.keys(),
                        map(_from_any, other.values()))
                )
                return Struct.from_any(other)

        if isinstance(other, (list, tuple, set)):
            # nested tuples are cells of cells, not cell arrays
            if _from_runtime:
                return Cell._from_runtime(other)
            else:
                return Cell.from_any(other)

        if isinstance(other, (np.ndarray, int, float, complex, bool)):
            # [array of] numbers -> Array
            if _from_runtime:
                return Array._from_runtime(other)
            else:
                return Array.from_any(other)

        if isinstance(other, str):
            return other

        if isinstance(other, bytes):
            return other.decode()

        if other is None:
            # This can happen when matlab code is called without `nargout`
            return other

        if not matlab:
            _import_matlab()

        if matlab and isinstance(other, matlab.object):
            return MatlabFunction.from_any(other)

        if type(other) in _matlab_array_types():
            return Array._from_runtime(other)

        if hasattr(other, "__iter__"):
            # Iterable -> let's try to make it a cell
            return cls.from_any(list(other), _from_runtime=_from_runtime)

        raise TypeError(
            f"Cannot convert {type(other)} into a matlab object."
        )

    @classmethod
    def _from_runtime(cls, obj):
        return cls.from_any(obj, _from_runtime=True)

    @classmethod
    def _to_runtime(cls, obj):
        """
        Convert object to representation that the matlab runtime understands.
        """
        to_runtime = cls._to_runtime

        if isinstance(obj, MatlabType):
            # class / structarray / cell
            return obj._as_runtime()

        elif isinstance(obj, (list, tuple, set)):
            return type(obj)(map(to_runtime, obj))

        elif isinstance(obj, dict):
            if "type__" in obj:
                return obj
            return type(obj)(zip(obj.keys(), map(to_runtime, obj.values())))

        elif isinstance(obj, np.ndarray):
            obj = np.asarray(obj)
            if obj.dtype in (object, dict):
                shape, dtype = obj.shape, obj.dtype
                obj = np.fromiter(map(to_runtime, obj.flat), dtype=dtype)
                obj = obj.reshape(shape)
                return obj.tolist()
            return obj

        elif sparse and isinstance(obj, sparse.sparray):
            return SparseArray.from_any(obj)._as_runtime()

        else:
            # TODO: do we want to raise if the type is not supported by matlab?
            #
            # Valid types for matlab bindings:
            #   - bool, int, float, complex, str, bytes, bytearray
            #
            # Valid matlab types that we have already dealt with:
            #   - list, tuple, set, dict, ndarray
            #
            # All other values/types are invalid (including `None`!)
            return obj

    def _as_runtime(self):
        raise NotImplementedError

    def _as_matlab_object(self):
        # Backward compatibility
        # FIXME: Or just keep `_as_matlab_object` and remove `_as_runtime`?
        return self._as_runtime()


class MatlabFunction(MatlabType):
    """
    Wrapper for matlab function handles.

    Example
    -------
    ```python
    times2 = Runtime.call("eval", "@(x) 2.*x")
    assert(time2(1) == 2)
    ```
    """

    def __init__(self, matlab_object):
        super().__init__()
        if not isinstance(matlab_object, matlab.object):
            raise TypeError("Expected a matlab.object")
        self._matlab_object = matlab_object

    def _as_runtime(self):
        return self._matlab_object

    @classmethod
    def _from_runtime(cls, other):
        return cls(other)

    @classmethod
    def from_any(cls, other):
        if isinstance(other, MatlabFunction):
            return other
        return cls._from_runtime(other)

    def __call__(self, *args, **kwargs):
        return Runtime.call(self._matlab_object, *args, **kwargs)


class AnyMatlabArray(MatlabType):
    """Base class for all matlab-like arrays (numeric, cell, struct)."""

    @property
    def as_num(self):
        raise TypeError(
            f"Cannot interpret a {type(self).__name__} as a numeric array"
        )

    @property
    def as_cell(self):
        raise TypeError(
            f"Cannot interpret a {type(self).__name__} as a cell"
        )

    @property
    def as_struct(self):
        raise TypeError(
            f"Cannot interpret a {type(self).__name__} as a struct"
        )

    # TODO: `as_obj` for object arrays?


# ----------------------------------------------------------------------
# DelayedArray
# ----------------------------------------------------------------------


class IndexOrKeyOrAttributeError(IndexError, KeyError, AttributeError):
    """
    Error raised when a non-indexing operation is performed on a
    non-finalized delayed array.
    """


class AnyDelayedArray(AnyMatlabArray):
    """
    This is an object that we return when we don't know how an indexed
    element will be used yet.

    It decides whether it is a Struct, Cell or Array based on the
    type of indexing that is used.

    In Matlab:
        * `a(x,y)   = num`  indicates that `a` is a numeric array;
        * `a(x,y)   = cell` indicates that `a` is a cell array;
        * `a{x,y}   = any`  indicates that `a` is a cell array;
        * `a(x,y).f = any`  indicates that `a` is a struct array;
        * `a.f      = any`  indicates that `a` is a struct.

    These indexing operations can be chained, so in
    `a(x).b.c{y}.d(z) = 2`:
        * `a`    is a struct array;
        * `b`    is a struct;
        * `c`    is a cell;
        * `c{y}` is a struct
        * `d`    is a numeric array.

    In Python, there is only one type of indexing (`[]`). This is a problem as
    we cannot differentiate `a{x}.b = y` -- where `a` is a cell that contains
    a struct -- from `a(x).b = y` --- where `a` is a struct array.

    One solution may be to abuse the "call" operator `()`, so that it returns a
    cell. This would work in some situations (`a[x].b = y` is a struct array,
    whereas `a(x).b = y` is a cell of struct). However, the statement
    `a(x) = y` (which would correspond to matlab's `a{x} = y`) is not valid
    python syntax. Furthermore, it would induce a new problem, as cells could
    not be differentiated from function handles, in some cases.

    Instead, the use of brackets automatically transforms the object into
    either:
    * a `Struct` (in all "get" cases, and in the "set" context `a[x] = y`,
      when `y` is either a `dict` or a `Struct`); or
    * a `Array` (in the "set" context `a[x] = y`, when `y` is neither a
      `dict` nor a `Struct`).

    Alternatively, if the user wishes to specify which type the object should
    take, we implement the properties `as_cell`, `as_struct` and `as_num`.

    Therefore:
    * `a[x,y]             = num`    : `a` is a numeric array;
    * `a[x,y]             = struct` : `a` is a numeric array;
    * `a[x,y].f           = any`    : `a` is a struct array;
    * `a(x,y).f           = any`    : `a` is a cell array containing a struct;
    * `a.f                = any`    : `a` is a struct.

    And explictly:
    * `a.as_cell[x,y]     = any`    : `a` is a cell array;
    * `a.as_struct[x,y].f = any`    : `a` is a struct array;
    * `a.as_cell[x,y].f   = any`    : `a` is a cell array containing a struct;
    * `a.as_num[x,y]      = num`    : `a` is a numeric array.
    """

    _ATTRIBUTES = ("_parent", "_index", "_future", "_finalized")

    def __init__(self, parent, *index):
        """
        Parameters
        ----------
        parent : ndarray | dict
            Reference to the object that will eventually contain
            this element.
            * If the containing array is a Cell, `parent` should be a
              `ndarray` view of that cell, and `index` should be a
              [tuple of] int.
            * If the containing array is a Struct, `parent` should be a
              `dict`, and `index` should be a string.
        index : str | [tuple of] int
            Index into the parent where this element will be inserted.
        """
        super().__init__()
        self._parent = parent       # reference to parent container
        self._index = index         # index into parent container
        self._future = None         # future array
        self._finalized = False     # whether this array has been finalized

    @property
    def _final(self):
        self._finalize()
        return self._future

    def _finalize(self):
        if self._finalized:
            return

        if self._future is None:
            # FIXME: I am not entirely sure this should ever happen
            self._future = _empty_array()

        # if future array is wrapped, unwrap it
        if isinstance(self._future, WrappedDelayedArray):
            self._future = self._future._future
            if hasattr(self._future, "_delayed_wrapper"):
                del self._future._delayed_wrapper

        # set value in parent
        parent = self._parent
        for index in self._index[:-1]:
            parent = parent[index]
        parent[self._index[-1]] = self._future

        # finalize parent if needed
        if hasattr(self._parent, "_final"):
            self._parent = self._parent._final

        self._finalized = True

    def _error_is_not_finalized(self, *args, **kwargs):
        raise IndexOrKeyOrAttributeError(
            "This DelayedArray has not been finalized, and you are "
            "attempting to use it in a way that may break its finalization "
            "cycle. It most likely means that you are indexing out-of-bounds "
            "without *setting* the out-of-bound value. "
            "Correct usage: `a.b(i).c = x` | Incorrect usage: `x = a.b(i).c`."
        )

    # Kill all operators
    __str__ = __repr__ = _error_is_not_finalized
    __bool__ = __float__ = __int__ = _error_is_not_finalized
    __ceil__ = __floor__ = __round__ = __trunc__ = _error_is_not_finalized
    __add__ = __iadd__ = __radd__ = _error_is_not_finalized
    __sub__ = __isub__ = __rsub__ = _error_is_not_finalized
    __mul__ = __imul__ = __rmul__ = _error_is_not_finalized
    __truediv___ = __itruediv___ = __rtruediv___ = _error_is_not_finalized
    __floordiv___ = __ifloordiv___ = __rfloordiv___ = _error_is_not_finalized
    __eq__ = __ne__ = _error_is_not_finalized
    __gt__ = __ge__ = __lt__ = __le__ = _error_is_not_finalized
    __abs__ = __neg__ = __pos__ = _error_is_not_finalized
    __pow__ = __ipow__ = __rpow__ = _error_is_not_finalized
    __mod__ = __imod__ = __rmod__ = _error_is_not_finalized
    __divmod__ = __idivmod__ = __rdivmod__ = _error_is_not_finalized
    __contains__ = _error_is_not_finalized

    def __getattribute__(self, name):
        # Do not allow any attribute to be accessed except for those
        # explicitly allowed by the AnyDelayedArray class.
        # This is so no "computation" is peformed on DelayedCell,
        # DelayedStruct, etc.
        if name.startswith("_"):
            return super().__getattribute__(name)
        if name not in self.__dict__ and name not in AnyDelayedArray.__dict__:
            return self._error_is_not_finalized()
        return super().__getattribute__(name)

    # --- Promise type -------------------------------------------------

    @property
    def as_cell(self) -> "DelayedCell":
        if self._future is None:
            self._future = DelayedCell((), self._parent, *self._index)
        if not isinstance(self._future, DelayedCell):
            raise TypeError(
                f"{type(self._future)} cannot be interpreted as a {Cell}"
            )
        return self._future

    @property
    def as_struct(self) -> "DelayedStruct":
        if self._future is None:
            self._future = DelayedStruct((), self._parent, *self._index)
        if not isinstance(self._future, DelayedStruct):
            raise TypeError(
                f"{type(self._future)} cannot be interpreted as a {Struct}"
            )
        return self._future

    @property
    def as_num(self) -> "DelayedArray":
        if self._future is None:
            self._future = DelayedArray([0], self._parent, *self._index)
        if not isinstance(self._future, DelayedArray):
            raise TypeError(
                f"{type(self._future)} cannot be interpreted as a {Array}"
            )
        return self._future

    def as_obj(self, obj):
        if (
            self._future is not None and
            not isinstance(self._future, MatlabClass)
        ):
            raise TypeError(
                f"{type(self._future)} cannot be interpreted as a {type(obj)}"
            )
        self._future = obj
        return self._future

    # --- Guess promised type ------------------------------------------

    def __call__(self, *index):
        return self.as_cell(*index)

    def __getitem__(self, index):
        return self.as_struct[index]

    def __getattr__(self, key):
        return self.as_struct[key]

    def __setitem__(self, index, value):
        if isinstance(index, str):
            arr = self.as_struct

        elif isinstance(value, MatlabClass):
            if index not in (0, -1):
                raise NotImplementedError(
                    "Implicit advanced indexing not implemented for",
                    type(value)
                )
            self.as_obj(value)
            return self._finalize()

        elif isinstance(value, (dict, Struct)):
            arr = self.as_struct
        elif isinstance(value, (tuple, list, set, Cell)):
            arr = self.as_cell
        elif isinstance(value, (int, float, np.number, Array)):
            arr = self.as_num
        elif isinstance(value, np.ndarray):
            if issubclass(value.dtype.type, np.number):
                arr = self.as_num
            else:
                arr = self.as_cell
        else:
            arr = self.as_cell

        arr[index] = value
        return self._finalize()  # Setter -> we can trigger finalize

    def __setattr__(self, key, value):
        if key in type(self)._ATTRIBUTES:
            return super().__setattr__(key, value)
        self.as_struct[key] = value
        return self._finalize()  # Setter -> we can trigger finalize


class WrappedDelayedArray(AnyDelayedArray):

    def __init__(self, future, parent, *index):
        super().__init__(parent, *index)
        self._future = future

    def __call__(self, *index):
        return self._future.__call__(*index)

    def __getitem__(self, index):
        return self._future.__getitem__(index)

    def __getattr__(self, key):
        return self._future.__getattr__(key)

    def __setitem__(self, index, value):
        self._future.__setitem__(index, value)
        self._finalize()

    def __setattr__(self, key, value):
        if key in type(self)._ATTRIBUTES:
            return super().__setattr__(key, value)
        self._future.__setattr__(key, value)
        self._finalize()


class DelayedStruct(WrappedDelayedArray):

    def __init__(self, shape, parent, *index):
        future = Struct.from_shape(shape)
        future._delayed_wrapper = self
        super().__init__(future, parent, *index)


class DelayedCell(WrappedDelayedArray):

    def __init__(self, shape, parent, *index):
        future = Cell.from_shape(shape)
        future._delayed_wrapper = self
        super().__init__(future, parent, *index)

        # Insert delayed arrays instead of the usual defaults
        opt = dict(
            flags=['refs_ok', 'zerosize_ok', 'multi_index'],
            op_flags=['writeonly', 'no_broadcast']
        )
        arr = np.ndarray.view(self._future, np.ndarray)
        with np.nditer(arr, **opt) as iter:
            for elem in iter:
                elem[()] = AnyDelayedArray(self, iter.multi_index)


class DelayedArray(WrappedDelayedArray):

    def __init__(self, shape, parent, *index):
        future = Array.from_shape(shape)
        future._delayed_wrapper = self
        super().__init__(future, parent, *index)


# ----------------------------------------------------------------------
# WrappedArray
# ----------------------------------------------------------------------


class AnyWrappedArray(AnyMatlabArray):
    """Base class for wrapped numpy/scipy arrays."""

    @classmethod
    def _parse_args(cls, *args, **kwargs):
        """
        This function is used in the __new__ constructor of Array/Cell/Struct.

        It does some preliminary preprocesing to reduces the number of
        cases that must be handled by __new__.

        In particular:
        - It converts multiple integer arguments to a single list[int]
        - It extracts the shape or object to copy, if there is one.
        - It convert positional dtype/order into keywords.

        Returns
        -------
        mode : {"shape", "obj"}
        arg : array-like | list[int]
        kwargs : dict
        """
        __has_dtype = kwargs.pop("__has_dtype", True)
        __has_order = kwargs.pop("__has_order", True)

        # Detect integer arguments
        args, shape, obj = list(args), [], None
        while args and isinstance(args[0], int):
            shape.append(args.pop(0))

        # If no integer arguments, the first argument (if it exists)
        # must be a shape or an array-like object to convert.
        if not shape:
            # Catch case where no size/array is passed and the first
            # argument is a data type.
            if args and not isinstance(args[0], (str, np.dtype, type)):
                obj = args.pop(0)

        # If there are positional arguments remaining, they are:
        # 1. dtype
        if args and __has_dtype:
            if "dtype" in kwargs:
                raise TypeError(
                    f"{cls.__name__}() got multiple values for "
                    f"argument 'dtype'"
                )
            kwargs["dtype"] = args.pop(0)
        # 2. order {"C", "F"}
        if args and __has_order:
            if "order" in kwargs:
                raise TypeError(
                    f"{cls.__name__}() got multiple values for "
                    f"argument 'order'"
                )
            kwargs["order"] = args.pop(0)
        # 3. no other positionals allowed -> raise
        if args:
            raise TypeError(
                f"{cls.__name__}() takes from 1 to 3 positional "
                "arguments but more were given"
            )

        # If we found an object and it is a generator
        # (= an iterable that has no `len`), copy its values into a list.
        if hasattr(obj, "__iter__") and not hasattr(obj, "__len__"):
            # save iterator values in a list
            obj = list(obj)

        # If obj is a list[int] -> it is a shape
        if (
            not shape and
            isinstance(obj, (list, tuple)) and
            all(isinstance(x, int) for x in obj)
        ):
            shape, obj = obj, None

        mode = "obj" if obj is not None else "shape"
        arg = obj if obj is not None else shape
        return mode, arg, kwargs


class WrappedArray(np.ndarray, AnyWrappedArray):
    """
    Base class for "arrays of things" (Array, Cell, Struct.)
    """

    # Value used to initalize empty arrays
    @classmethod
    def _DEFAULT(cls, shape: list = ()):
        raise NotImplementedError

    def __str__(self):
        fmt = {"all": str}  # use str instead of repr for items
        return np.array2string(self, separator=", ", formatter=fmt)

    def __repr__(self):
        # close to np.array_repr, but hides dtype.
        pre = type(self).__name__ + "("
        suf = ")"
        return (
            pre +
            np.array2string(self, prefix=pre, suffix=suf, separator=", ") +
            suf
        )

    def __bool__(self):
        # NumPy arrays do not lower to True/False in a boolean context.
        # We do lower our matlab equivalent using all()
        return np.ndarray.view(np.all(self), np.ndarray).item()

    def __iter__(self):
        # FIXME:
        #   ndarray.__iter__ seems to call __getattr__, which leads
        #   to infinite resizing.
        #   This overload seems to fix it, but may not be computationally
        #   optimal.
        for i in range(len(self)):
            yield self[i]

    def __getitem__(self, index):
        """Resize array if needed, then fallback to np.ndarray indexing."""
        try:
            return super().__getitem__(index)
        except IndexError:
            # We return a delayed version of the current type, with the
            # same shape as the requested view. Its elements will only
            # be inserted into the original object (self) is the view
            # is properly finalized by an eventual call to __setitem__
            # or __setattr__.
            return self._return_delayed(index)

    def __setitem__(self, index, value):
        """Resize array if needed, then fallback to np.ndarray indexing."""
        value = MatlabType.from_any(value)
        try:
            return super().__setitem__(index, value)
        except (IndexError, ValueError):
            self._resize_for_index(index)
            return super().__setitem__(index, value)

    def __delitem__(self, index):
        if isinstance(index, tuple):
            raise TypeError(
                "Multidimensional indices are not supported in `del`."
            )

        # --- list: delete sequentially, from tail to head -------------
        if hasattr(index, "__iter__"):
            index = (len(self) + i if i < 0 else i for i in index)
            index = sorted(index, reverse=True)
            for i in index:
                del self[i]

        # --- slice: skip the entire slice, if possible ----------------
        elif isinstance(index, slice):
            start, stop, step = index.start, index.stop, index.step

            # --- let's make the slice parameters a bit more useful ---
            step = step or 1
            # compute true start
            if start is None:
                if step < 0:
                    start = len(self) - 1
                else:
                    start = 0
            if start < 0:
                start = len(self) + start
            # compute stop in terms of "positive indices"
            # (where -1 really means -1, and not n-1)
            if stop is not None:
                if stop < 0:
                    stop = len(self) + stop
            else:
                stop = len(self) if step > 0 else -1
            stop = min(stop, len(self)) if step > 0 else max(stop, -1)
            # align stop with steps
            stop = start + int(np.ceil(abs(stop - start) / abs(step))) * step
            # compute true inclusive stop
            stop_inclusive = stop - step
            # ensure step is positive
            if step < 0:
                start, stop_inclusive, step = stop_inclusive, start, abs(step)

            # --- if non consecutive, fallback to sequential ---
            if step != 1:
                index = range(start, stop+1, step)
                del self[index]

            # --- otherwise, skip the entire slice ---
            else:
                nb_del = 1 + stop_inclusive - start
                new_shape = list(np.shape(self))
                new_shape[0] -= nb_del
                self[start:-nb_del] = self[stop_inclusive:]
                np.ndarray.resize(self, new_shape, refcheck=False)

        # --- int: skip a single element -------------------------------
        else:
            index = int(index)
            if index < 0:
                index = len(self) + index
            new_shape = list(np.shape(self))
            new_shape[0] -= 1
            self[index:-1] = self[index+1:]
            np.ndarray.resize(self, new_shape, refcheck=False)

    def _resize_for_index(self, index, set_default=True):
        """
        Resize the array so that the (multidimensional) index is not OOB.

        We only support a restricted number of cases:
            * Index should only contain integers and slices
              (no smart indexing, no new axis, no ellipsis)
            * Only integer indices are used to compute the new size.
              This is to be consistent with numpy, where slice-indexing never
              raises IndexError (but instead returns the overlap between
              the array and the slice -- eventually empty).

        Other cases could be handled but require much more complicated logic.
        """
        input_shape = self.shape
        if not isinstance(index, tuple):
            index = (index,)
        index, new_index = list(index), []
        shape, new_shape = list(np.shape(self)), []
        axis = -1
        while index:
            next_index = index.pop(0)
            if shape:
                next_shape = shape.pop(0)
            else:
                next_shape = 1
            axis += 1
            if isinstance(next_index, int):
                if next_index < 0:
                    next_index = next_shape + next_index
                if next_index >= next_shape:
                    next_shape = next_index + 1
            elif isinstance(next_index, slice):
                # FIXME: this is not exactly right when abs(step) != 1
                step = next_index.step or 1
                start = next_index.start
                stop = next_index.stop
                start = next_shape + start if start < 0 else start
                stop = next_shape + stop if stop < 0 else stop
                if step < 0:
                    max_index = start
                else:
                    max_index = stop
                if max_index is None:
                    max_index = next_shape
                if max_index > next_shape:
                    next_shape = max_index
            elif not isinstance(next_index, slice):
                raise TypeError(
                    "Can only automatically resize cell if simple "
                    "indexing (int, slice) is used."
                )
            new_index.append(next_index)
            new_shape.append(next_shape)
        new_shape = new_shape + shape
        if not input_shape:
            # We risk erasing the original scalar whn setting the
            # defaults, so we save it and reinsert it at the end.
            scalar = np.ndarray.view(self, np.ndarray).item()
        np.ndarray.resize(self, new_shape, refcheck=False)
        if set_default:
            arr = np.ndarray.view(self, np.ndarray)
            view_index = tuple(slice(x, None) for x in input_shape)
            view_shape = arr[view_index].shape
            new_data = self._DEFAULT(view_shape)
            arr[view_index] = new_data
            if not input_shape:
                # Insert back scalar in the first position.
                scalar_index = (0,) * arr.ndim
                arr[scalar_index] = scalar

    def _return_delayed(self, index):
        if not isinstance(index, tuple):
            index = (index,)

        #   Resize as if we were already performing a valid __setitem__.
        #   This helps us guess the shape of the view.
        #   Also, we'll hopefully be able to use the allocated space
        #   later if the caller did not mess up their syntax, so there's
        #   not much wasted performance.
        shape = self.shape
        self._resize_for_index(index, set_default=False)

        #   Ensure that the indexed view is an array, not a single item.
        index_for_view = index
        if ... not in index_for_view:
            index_for_view = index_for_view + (...,)

        sub_shape = np.ndarray.view(self, np.ndarray)[index_for_view].shape

        #   Now, undo resize so that if the caller's syntax is wrong and
        #   an exception is raised (and caught), it's as if nothing ever
        #   happened.
        np.ndarray.resize(self, shape, refcheck=False)

        #   If self is wrapped in a DelayedCell/DelayedStruct,
        #   reference wrapper instead of self.
        parent = getattr(self, "_delayed_wrapper", self)

        if isinstance(self, Cell):
            if sub_shape == ():
                return AnyDelayedArray(parent, index)
            else:
                return DelayedCell(sub_shape, parent, index)

        elif isinstance(self, Struct):
            return DelayedStruct(sub_shape, parent, index)

        else:
            #   In numeric arrays, only seeting OOB items is allowed.
            #   Getting OOB items should raise an error, which this
            #   call to the ndarray accessor will do.
            return super().__getitem__(index)


# ----------------------------------------------------------------------
# Array
# ----------------------------------------------------------------------


class _ListishMixin:
    """These methods are implemented in Cell and Array, but not Struct."""

    # TODO:
    #   The following _ListLike methods could potentially be moved here
    #   (i.e., be implemented in Array as well as Cell):
    #
    #   * index
    #   * count
    #   * reverse
    #   * pop
    #   * remove

    def append(self, value):
        """
        Append object to the end of the list
        (along the first dimension).
        """
        new_shape = list(np.shape(self))
        new_shape[0] += 1
        np.ndarray.resize(self, new_shape, refcheck=False)
        self[-1] = value

    def extend(self, value):
        """
        Extend list by appending elements from the iterable
        (along the first dimension).
        """
        value = type(self).from_any(value)
        init_len = len(self)
        batch = len(self) + len(value)
        shape = np.broadcast_shapes(np.shape(self)[1:], np.shape(value)[1:])
        new_shape = [batch] + list(shape)
        np.ndarray.resize(self, new_shape, refcheck=False)
        self[init_len:] = value

    def clear(self):
        """Remove all items by setting the first axis to have size 0."""
        zero_shape = list(np.shape(self))
        zero_shape[0] = 0
        np.ndarray.resize(zero_shape, refcheck=False)


class Array(_ListishMixin, WrappedArray):
    """
    Numeric array, compatible with matlab arrays.

    ```python
    # Instantiate from size
    Array(N, M, ...)
    Array([N, M, ...])
    Array.from_shape([N, M, ...])

    # Instantiate from existing numeric array
    Array(other_array)
    Array.from_any(other_array)

    # Other options
    Array(..., dtype=None, order=None, *, copy=None, owndata=None)
    ```

    !!! warning
        Lists or vectors of integers can be interpreted as shapes or as
        numeric arrays to copy. They are interpreted as shapes by the
        `Array` constructor. To ensure that they are interpreted as
        arrays to copy, use `Array.from_any`.
    """
    @classmethod
    def _DEFAULT(cls, n: list = ()) -> int:
        return 0

    def __new__(cls, *args, **kwargs) -> "Array":
        mode, arg, kwargs = cls._parse_args(*args, **kwargs)
        if mode == "shape":
            obj = super().__new__(cls, shape=arg, **kwargs)
            obj[...] = cls._DEFAULT()
            if not issubclass(obj.dtype.type, np.number):
                raise TypeError("Array data type must be numeric")
            return obj
        else:
            return cls.from_any(arg, **kwargs)

    def _as_runtime(self) -> np.ndarray:
        return np.ndarray.view(self, np.ndarray)

    @classmethod
    def _from_runtime(cls, other) -> "Array":
        other = np.asarray(other)
        if len(other.shape) == 2 and other.shape[0] == 1:
            other = other.squeeze(0)
        return np.ndarray.view(other, cls)

    @classmethod
    def from_shape(cls, shape=tuple(), **kwargs) -> "Array":
        """
        Build an array of a given shape.

        Parameters
        ----------
        shape : list[int]
            Shape of new array.

        Other Parameters
        ----------------
        dtype : np.dtype | None, default='double'
            Target data type.
        order : {"C", "F"} | None, default=None
            Memory layout.
            * "C" row-major (C-style);
            * "F" column-major (Fortran-style);

        Returns
        -------
        array : Array
            New array.
        """
        # Implement in __new__ so that array owns its data
        return cls(list(shape), **kwargs)

    @classmethod
    def from_any(cls, other, **kwargs) -> "Array":
        """
        Convert an array-like object to a numeric array.

        Parameters
        ----------
        other : ArrayLike
            object to convert.

        Other Parameters
        ----------------
        dtype : np.dtype | None, default=None
            Target data type. Guessed if `None`.
        order : {"C", "F", "A", "K"} | None, default=None
            Memory layout.
            * "C" row-major (C-style);
            * "F" column-major (Fortran-style);
            * "A" (any) means "F" if a is Fortran contiguous, "C" otherwise;
            * "K" (keep) preserve input order;
            * `None` preserve input order if possible, "C" otherwise.
        copy : bool | None, default=None
            Whether to copy the underlying data.
            * `True` : the object is copied;
            * `None` : the the object is copied only if needed;
            * `False`: raises a `ValueError` if a copy cannot be avoided.
        owndata : bool, default=None
            If True, ensures that the returned Array owns its data.
            This may trigger an additional copy.

        Returns
        -------
        array : Array
            Converted array.
        """
        # prepare for copy
        owndata = kwargs.pop("owndata", False)
        copy = None if owndata else kwargs.pop("copy", None)
        inp = other

        # ensure array
        other = np.asanyarray(other, **kwargs)
        if not issubclass(other.dtype.type, np.number):
            if kwargs.get("dtype", None):
                # user-specified non numeric type -> raise
                raise TypeError("Array data type must be numeric")
            other = np.asanyarray(other, dtype=np.float64, **kwargs)

        # view as Array
        other = np.ndarray.view(other, cls)

        # copy (after view so that output owns data if copy=True)
        other = _copy_if_needed(other, inp, copy)

        # take ownership
        if owndata:
            tmp = other
            other = cls(tmp.shape, strides=tmp.strides)
            other[...] = tmp

        return other

    @classmethod
    def from_cell(cls, other: "Cell", **kwargs) -> "Array":
        """
        Convert a `Cell` to a numeric `Array`.

        Parameters
        ----------
        other : Cell
            Cell to convert.

        Other Parameters
        ----------------
        dtype : np.dtype | None, default=None
            Target data type. Guessed if `None`.
        order : {"C", "F", "A", "K"} | None, default="K"
            Memory layout.
            * "C" row-major (C-style);
            * "F" column-major (Fortran-style);
            * "A" (any) means "F" if a is Fortran contiguous, "C" otherwise;
            * "K" (keep) preserve input order.
        owndata : bool, default=None
            If True, ensures that the returned Array owns its data.
            This may trigger an additional copy.

        Returns
        -------
        array : Array
            Converted array.
        """
        if not isinstance(other, Cell):
            raise TypeError(f"Expected a {Cell} but got a {type(other)}")
        order = kwargs.get("order", None)
        if order in (None, "K", "A"):
            order = (
                "F" if other.flags.f_contiguous else
                "C" if other.flags.c_contiguous else
                order)
            kwargs["order"] = order
        return cls.from_any(other.tolist(), **kwargs)

    @property
    def as_num(self) -> "Array":
        return self

    def __repr__(self):
        if self.ndim == 0:
            # Scalar -> display as python scalar
            return np.array2string(self, separator=", ")
        else:
            return super().__repr__()


# ----------------------------------------------------------------------
# SparseArray
# ----------------------------------------------------------------------


class _SparseMixin:
    """Methods common to the scipy.sparse and dense backends."""

    def _as_runtime(self) -> dict:
        indices = self.nonzero()
        values = self[indices].reshape([-1, 1])
        indices = np.stack(indices, -1)
        indices += 1
        size = np.array([[*np.shape(self)]])
        return dict(
            type__='sparse',
            size__=size,
            indices__=indices,
            values__=values,
        )

    @classmethod
    def _from_runtime(cls, dictobj: dict) -> "SparseArray":
        if dictobj['type__'] != 'sparse':
            raise ValueError("Not a matlab sparse matrix")
        size = np.array(dictobj['size__'], dtype=np.uint64).ravel()
        size = size.tolist()
        dtype = _matlab_array_types()[type(dictobj['values__'])]
        indices = np.asarray(dictobj['indices__'], dtype=np.long) - 1
        values = np.asarray(dictobj['values__'], dtype=dtype).ravel()
        return cls.from_coo(values, indices.T, size)


if sparse:

    class WrappedSparseArray(sparse.sparray, AnyWrappedArray):
        """Base class for sparse arrays."""

        def to_dense(self) -> "Array":
            return Array.from_any(self.todense())

    class SparseArray(sparse.csc_array, _SparseMixin, WrappedSparseArray):
        """
        Matlab sparse arrays (scipy.sparse backend).

        ```python
        # Instantiate from size
        SparseArray(N, M, ...)
        SparseArray([N, M, ...])
        SparseArray.from_shape([N, M, ...])

        # Instantiate from existing sparse or dense array
        SparseArray(other_array)
        SparseArray.from_any(other_array)

        # Other options
        SparseArray(..., dtype=None, *, copy=None)
        ```

        !!! warning
            Lists or vectors of integers can be interpreted as shapes
            or as dense arrays to copy. They are interpreted as shapes
            by the `SparseArray` constructor. To ensure that they are
            interpreted as dense arrays to copy, usse `SparseArray.from_any`.
        """

        def __init__(self, *args, **kwargs) -> None:
            mode, arg, kwargs = self._parse_args(*args, **kwargs)
            if mode == "shape":
                ndim = len(arg)
                return super().__init__(([], [[]]*ndim), shape=arg, **kwargs)
            else:
                if not isinstance(arg, (np.ndarray, sparse.sparray)):
                    arg = np.asanyarray(arg)
                return super().__init__(arg, **kwargs)

        @classmethod
        def from_coo(cls, values, indices, shape=None, **kw) -> "SparseArray":
            """
            Build a sparse array from indices and values.

            Parameters
            ----------
            values : (N,) ArrayLike
                Values to set at each index.
            indices : (D, N) ArrayLike
                Indices of nonzero elements.
            shape : list[int] | None
                Shape of the array.
            dtype : np.dtype | None
                Target data type. Same as `values` by default.

            Returns
            -------
            array : SparseArray
                New array.
            """
            indices = np.asarray(indices)
            coo = sparse.coo_array((values, indices), shape=shape, **kw)
            return cls.from_any(coo)

        @classmethod
        def from_shape(cls, shape=tuple(), **kwargs) -> "SparseArray":
            """
            Build an array of a given shape.

            Parameters
            ----------
            shape : list[int]
                Shape of the new array.

            Other Parameters
            ----------------
            dtype : np.dtype | None, default='double'
                Target data type.

            Returns
            -------
            array : SparseArray
                New array.
            """
            return cls(list(shape), **kwargs)

        @classmethod
        def from_any(cls, other, **kwargs) -> "SparseArray":
            """
            Convert an array-like object to a numeric array.

            Parameters
            ----------
            other : ArrayLike
                object to convert.

            Other Parameters
            ----------------
            dtype : np.dtype | None, default=None
                Target data type. Guessed if `None`.
            copy : bool | None, default=None
                Whether to copy the underlying data.
                * `True` : the object is copied;
                * `None` : the the object is copied only if needed;
                * `False`: raises a `ValueError` if a copy cannot be avoided.

            Returns
            -------
            array : SparseArray
                Converted array.
            """
            copy = kwargs.pop("copy", None)
            inp = other
            if not isinstance(other, sparse.sparray):
                other = np.asanyarray(other, **kwargs)
            other = cls(other, **kwargs)
            other = _spcopy_if_needed(other, inp, copy)
            return other

else:
    warnings.warn(
        "Since scipy.sparse is not available, sparse matrices "
        "will be implemented as dense matrices, which can lead to "
        "unsubstainable memory usage. If this is an issue, install "
        "scipy in your python environment."
    )

    class SparseArray(_SparseMixin, Array):
        """
        Matlab sparse arrays (dense backend).

        ```python
        # Instantiate from size
        SparseArray(N, M, ...)
        SparseArray([N, M, ...])
        SparseArray.from_shape([N, M, ...])

        # Instantiate from existing sparse or dense array
        SparseArray(other_array)
        SparseArray.from_any(other_array)

        # Other options
        SparseArray(..., dtype=None, *, copy=None)
        ```

        !!! warning
            Lists or vectors of integers can be interpreted as shapes
            or as dense arrays to copy. They are interpreted as shapes
            by the `SparseArray` constructor. To ensure that they are
            interpreted as dense arrays to copy, usse `SparseArray.from_any`.

        !!! note
            This is not really a sparse array, but a dense array that gets
            converted to a sparse array when passed to matlab.
        """

        def to_dense(self) -> "Array":
            return np.ndarray.view(self, Array)

        @classmethod
        def from_coo(cls, values, indices, shape=None, **kw) -> "SparseArray":
            """
            Build a sparse array from indices and values.

            Parameters
            ----------
            values : (N,) ArrayLike
                Values to set at each index.
            indices : (D, N) ArrayLike
                Indices of nonzero elements.
            shape : list[int] | None
                Shape of the array.
            dtype : np.dtype | None
                Target data type. Same as `values` by default.

            Returns
            -------
            array : SparseArray
                New array.
            """
            dtype = kw.get("dtype", None)
            indices = np.asarray(indices)
            values = np.asarray(values, dtype=dtype)
            if shape is None:
                shape = (1 + indices.max(-1)).astype(np.uint64).tolist()
            if dtype is None:
                dtype = values.dtype
            obj = cls.from_shape(shape, dtype=dtype)
            obj[tuple(indices)] = values
            return obj


# ----------------------------------------------------------------------
# Cell
# ----------------------------------------------------------------------


class _ListMixin(_ListishMixin, MutableSequence):
    """These methods are implemented in Cell, but not in Array or Struct."""

    # NOTE:
    #   The only abstract methods from MutableSequence are:
    #   * __getitem__   -> inherited from WrappedArray
    #   * __setitem__   -> inherited from WrappedArray
    #   * __delitem__   -> implemented here
    #   * __len__       -> inherited from np.ndarray
    #   * insert        -> implemented here
    #
    #   MutableSequence implements the following non-abstract methods,
    #   but we overload them for speed:
    #   * index         -> implemented here
    #   * count         -> implemented here
    #   * append        -> inherited from _ListishMixin
    #   * clear         -> inherited from _ListishMixin
    #   * reverse       -> implemented here
    #   * extend        -> inherited from _ListishMixin
    #   * pop           -> implemented here
    #   * remove        -> implemented here
    #   * __iter__      -> inherited from np.ndarray
    #   * __reversed__  -> inherited from Sequence
    #   * __iadd__      -> implemented here
    #   * __eq__        -> implemented here
    #   * __ne__        -> implemented here
    #   * __ge__        -> implemented here
    #   * __gt__        -> implemented here
    #   * __le__        -> implemented here
    #   * __lt__        -> implemented here
    #
    #   Mutable implements the following non-abstract method, whose
    #   behaviour differs from that of np.ndarray.
    #   We use np.ndarray's instead.
    #   * __contains__  -> inherited from np.ndarray

    # --- ndarray ------------------------------------------------------

    # need to explicitely reference np.ndarray methods otherwise it
    # goes back to MutableSequence, which raises.
    __len__ = WrappedArray.__len__
    __getitem__ = WrappedArray.__getitem__
    __setitem__ = WrappedArray.__setitem__
    __delitem__ = WrappedArray.__delitem__
    __contains__ = WrappedArray.__contains__
    __iter__ = WrappedArray.__iter__

    # --- magic --------------------------------------------------------

    def __add__(self, other):
        other = type(self).from_any(other)
        return np.concatenate([self, other])

    def __radd__(self, other):
        other = type(self).from_any(other)
        return np.concatenate([other, self])

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __mul__(self, value):
        return np.concatenate([self] * value)

    def __rmul__(self, value):
        return np.concatenate([self] * value)

    def __imul__(self, value):
        length = len(self)
        new_shape = list(np.shape(self))
        new_shape[0] *= value
        np.ndarray.resize(self, new_shape, refcheck=False)
        for i in range(1, value):
            self[i*length:(i+1)*length] = self[:length]
        return self

    # In lists, __contains__ should be treated as meaning "contains this
    # element along the first dimension." I.e.,
    # `value in sequence` should be equivalent to `value in iter(sequence)`.
    #
    # In contrast, ndarray's __contains__ is used "element-wise".
    # I.e., it is equivalent to `value in sequence.flat`.
    # It is the main reason ndarray do not implement the MutableSequence
    # protocol:
    # https://github.com/numpy/numpy/issues/2776#issuecomment-652584346
    #
    # We use the numpy behaviour, and implement list_contains to recover
    # the list behaviour.

    def list_contains(self, value, broadcast=True):
        """
        Check whether a value is in the object, when iterated along its
        first dimension.

        Should be roughly equivalent to `value in iter(self)`, although
        it also takes care of collapsing boolean arrays into a single
        boolean by calling `all()` on them.

        * If `broadcast=True` (default), equality is loose in the sense
          that `1` matches `[1, 1, 1]`.
        * If `broadcast=False`, array-like objects only match if they
          have the exact same shape.
        """
        value = np.asarray(value)
        for elem in self:
            elem = np.asarray(elem)
            if not broadcast and value.shape != elem.shape:
                continue
            if (elem == value).all():
                return True
        return False

    # --- sequence -----------------------------------------------------

    def count(self, value, broadcast=True):
        """
        Return number of occurrences of value, when iterating along the
        object's first dimension.

        * If `broadcast=True` (default), equality is loose in the sense
          that `1` matches `[1, 1, 1]`.
        * If `broadcast=False`, array-like objects only match if they
          have the exact same shape.
        """
        value = np.asarray(value)

        def iter():
            for elem in self:
                elem = np.asarray(elem)
                if not broadcast and value.shape != elem.shape:
                    yield False
                yield bool((elem == value).all())

        return sum(iter())

    def index(self, value, broadcast=True):
        """
        Return first index of value, when iterating along the object's
        first dimension.

        * If `broadcast=True` (default), equality is loose in the sense
          that `1` matches `[1, 1, 1]`.
        * If `broadcast=False`, array-like objects only match if they
          have the exact same shape.
        """
        value = np.asarray(value)
        for i, elem in enumerate(self):
            elem = np.asarray(elem)
            if not broadcast and value.shape != elem.shape:
                continue
            if (elem == value).all():
                return i
        raise ValueError(value, "is not in", type(self).__name__)

    def insert(self, index, obj):
        """Insert object before index."""
        if index < 0:
            # +1 because we insert *after* the index if negative
            index = len(self) + index + 1
        if not isinstance(index, int):
            raise TypeError("Only scalar elements can be inserted.")
        new_shape = list(np.shape(self))
        new_shape[0] += 1
        np.ndarray.resize(self, new_shape, refcheck=False)
        self[index+1:] = self[index:-1]
        self[index] = obj

    def pop(self, index=-1):
        """Remove and return item at index (default last)."""
        if index < 0:
            index = len(self) + index
        # need to copy as its memory location will be overwritten by del
        if not isinstance(index, int):
            raise TypeError("Only scalar indices can be popped.")
        value = np.copy(self[index])
        del self[index]
        return value

    def remove(self, value):
        """Remove first occurrence of value."""
        new_shape = list(np.shape(self))
        new_shape[0] -= 1
        index = self.index(value)
        del self[index]

    def reverse(self):
        """Reverse *IN PLACE*."""
        self[:] = self[::-1]

    def sort(self, *, key=None, reverse=False, kind="stable", axis=0):
        """
        Sort the list in ascending order and return None.

        The sort is in-place (i.e. the list itself is modified) and stable
        (i.e. the order of two equal elements is maintained).

        If a key function is given, apply it once to each list item and sort
        them, ascending or descending, according to their function values.

        The reverse flag can be set to sort in descending order.

        !!! note
            We further expose options from `np.ndarray.sort`, which is used
            under the hood. However, we use different defaults
            (kind="stable" instead of "quicksort", axis=0 instead of -1).

            If `key` is provided, we fallback to `list.sort`
            (triggers a temporary copy).
        """
        if key:
            aslist = list(np.moveaxis(self, axis, 0))
            aslist.sort(key=key, reverse=reverse)
            asarray = np.stack(aslist, axis=axis)
            self[...] = asarray
        else:
            np.ndarray.sort(self, kind=kind, axis=axis)
            if reverse:
                self.reverse()


class Cell(_ListMixin, WrappedArray):
    """
    Cell array, compatible with matlab cells.

    ```python
    # Instantiate from size
    Cell(N, M, ...)
    Cell([N, M, ...])
    Cell.from_shape([N, M, ...])

    # Instantiate from existing (cell-like) array (implicitely)
    Cell(cell_like)
    Cell.from_any(cell_like)

    # Other options
    Cell(..., order=None, *, copy=None, owndata=None, deepcat=False)
    ```

    A cell is a `MutableSequence` and therefore (mostly) behaves like a list.
    It implements the following methods (which all operate along the
    1st dimension, if the cell is a cell array):

    * `append`        : Append object to the end of the cell
    * `clear`         : Empty the cell
    * `count`         : Number of occurrences of a value
    * `extend`        : Extend list by appending elements from the iterable
    * `index`         : First index of a value
    * `insert`        : Insert object before index
    * `pop`           : Remove and return item at index
    * `remove`        : Remove first occurrence of value
    * `reverse`       : Reverse the cell in-place
    * `sort`          : Sort the list in ascending order in-place

    The magic operators `+` and `*` also operate as in lists:

    * `a + b`         : Concatenate `a` and `b`
    * `a += b`        : Append iterable `b` to `a`
    * `a * n`         : Concatenate `n` repeats of `a`
    * `a *= n`        : Append `n` repeats of `a` to `a`

    Finally, elements (along the first dimension) can be deleted using
    `del cell[index]`.

    !!! warning
        Lists or vectors of integers can be interpreted as shapes or as
        cell-like objects to copy. They are interpreted as shapes by the
        `Cell` constructor. To ensure that they are interpreted as
        arrays to copy, use `Cell.from_any`.
    """

    # NOTE
    #   _ListMixin must have precedence over _WrappedArray so that its
    #   method overload those from np.ndarray. This is why the
    #   inheritence order is (_ListMixin, _WrappedArray).

    _DelayedType = DelayedCell

    @classmethod
    def _DEFAULT(cls, shape: list = ()) -> np.ndarray:
        data = np.empty(shape, dtype=object)
        opt = dict(
            flags=['refs_ok', 'zerosize_ok'],
            op_flags=['writeonly', 'no_broadcast']
        )
        with np.nditer(data, **opt) as iter:
            for elem in iter:
                elem[()] = _empty_array()
        return data

    def _fill_default(self):
        arr = np.ndarray.view(self, np.ndarray)
        opt = dict(flags=['refs_ok', 'zerosize_ok'],
                   op_flags=['writeonly', 'no_broadcast'])
        with np.nditer(arr, **opt) as iter:
            for elem in iter:
                elem[()] = _empty_array()
        return self

    def __new__(cls, *args, **kwargs) -> "Cell":
        mode, arg, kwargs = cls._parse_args(*args, **kwargs)
        kwargs["dtype"] = object
        if mode == "shape":
            if len(arg) == 0:
                # Scalar cells are forbidden
                arg = [0]
            return super().__new__(cls, shape=arg, **kwargs)._fill_default()
        else:
            return cls.from_any(arg, **kwargs)

    def _as_runtime(self) -> dict:
        if self.ndim == 1:
            return MatlabType._to_runtime(self.tolist())
        else:
            size = np.array([[*np.shape(self)]])
            data = np.ndarray.view(self, np.ndarray)
            data = np.reshape(data, [-1], order="F").tolist()
            data = MatlabType._to_runtime(data)
            return dict(type__='cell', size__=size, data__=data)

    @classmethod
    def _from_runtime(cls, objdict: dict) -> "Cell":
        if isinstance(objdict, (list, tuple, set)):
            shape = [len(objdict)]
            objdict = dict(type__='cell', size__=shape, data__=objdict)

        if objdict['type__'] != 'cell':
            raise TypeError('objdict is not a cell')

        size = np.array(objdict['size__'], dtype=np.uint64).ravel()
        if len(size) == 2 and size[0] == 1:
            # NOTE: should not be needed for Cell, as this should
            # have been taken care of by MPython, but I am keeping it
            # here for symmetry with Array and Struct.
            size = size[1:]
        data = np.fromiter(objdict['data__'], dtype=object)
        data = data.reshape(size[::-1]).transpose()
        try:
            obj = data.view(cls)
        except Exception:
            raise RuntimeError(
                f'Failed to construct Cell data:\n'
                f'  data={data}\n'
                f'  objdict={objdict}'
            )

        # recurse
        opt = dict(flags=['refs_ok', 'zerosize_ok'],
                   op_flags=['readwrite', 'no_broadcast'])
        with np.nditer(data, **opt) as iter:
            for elem in iter:
                elem[()] = MatlabType._from_runtime(elem.item())

        return obj

    @classmethod
    def from_shape(cls, shape=tuple(), **kwargs) -> "Cell":
        """
        Build a cell array of a given size.

        Parameters
        ----------
        shape : list[int]
            Input shape.

        Other Parameters
        ----------------
        order : {"C", "F"} | None, default="C"
            Memory layout.
            * "C" row-major (C-style);
            * "F" column-major (Fortran-style).

        Returns
        -------
        cell : Cell
            New cell array.

        """
        # Implement in __new__ so that cell owns its data
        return cls(list(shape), **kwargs)

    @classmethod
    def from_any(cls, other, **kwargs) -> "Cell":
        """
        Convert a (nested) list-like object to a cell.

        Parameters
        ----------
        other : CellLike
            object to convert.

        Other Parameters
        ----------------
        deepcat : bool, default=False
            Convert cells of cells into cell arrays.
        order : {"C", "F", "A", "K"} | None, default=None
            Memory layout.
            * "C" row-major (C-style);
            * "F" column-major (Fortran-style);
            * "A" (any) means "F" if a is Fortran contiguous, "C" otherwise;
            * "K" (keep) preserve input order;
            * `None` preserve input order if possible, "C" otherwise.
        copy : bool | None, default=None
            Whether to copy the underlying data.
            * `True` : the object is copied;
            * `None` : the the object is copied only if needed;
            * `False`: raises a `ValueError` if a copy cannot be avoided.
        owndata : bool, default=False
            If True, ensures that the returned Cell owns its data.
            This may trigger an additional copy.

        Returns
        -------
        cell : Cell
            Converted cell.
        """
        # matlab object
        if isinstance(other, dict) and "type__" in other:
            return cls._from_runtime(other)

        kwargs["dtype"] = object
        deepcat = kwargs.pop("deepcat", False)

        # prepare for copy
        owndata = kwargs.pop("owndata", False)
        copy = None if owndata else kwargs.pop("copy", None)
        inp = other

        # recursive shallow conversion
        if not deepcat:
            # make sure matlab is imported so that we can detect
            # matlab arrays.
            _import_matlab()

            # This is so list[list] are converted to Cell[Cell] and
            # not to a 2D Cell array.
            def asrecursive(other):
                if isinstance(other, tuple(_matlab_array_types())):
                    dtype = _matlab_array_types()[type(other)]
                    other = np.asarray(other, dtype=dtype)
                if isinstance(other, (np.ndarray, AnyDelayedArray)):
                    return other
                elif isinstance(other, (str, bytes)):
                    return other
                elif hasattr(other, "__iter__"):
                    other = list(map(asrecursive, other))
                    tmp = np.ndarray(len(other), dtype=object)
                    for i, x in enumerate(other):
                        tmp[i] = x
                    other = tmp
                    obj = np.ndarray.view(other, cls)
                    return obj
                else:
                    return other

            other = asrecursive(other)

            if not isinstance(other, np.ndarray):
                other = np.asanyarray(other, **kwargs)

        # deep conversion
        else:
            other = np.asanyarray(other, **kwargs)
            other = cls._unroll_build(other)

        # as cell
        other = np.ndarray.view(other, cls)

        # copy (after view so that output owns data if copy=True)
        other = _copy_if_needed(other, inp, copy)

        # take ownership
        if owndata:
            tmp = other
            other = cls(tmp.shape, strides=tmp.strides)
            other[...] = tmp

        # recurse
        opt = dict(flags=['refs_ok', 'zerosize_ok'],
                   op_flags=['readwrite', 'no_broadcast'])
        with np.nditer(other, **opt) as iter:
            for elem in iter:
                elem[()] = MatlabType.from_any(elem.item())

        return other

    # aliases
    from_num = from_array = from_any

    @classmethod
    def _unroll_build(cls, arr):
        # The logic here is that we may sometimes end up with cells of
        # cells that must be converted to deep cell arrays.
        # To circumvent this, we find elements that are arrays, convert
        # them to lists, and recurse.
        rebuild = False
        arr = np.asarray(arr)
        opt = dict(flags=['refs_ok', 'zerosize_ok'],
                   op_flags=['readwrite', 'no_broadcast'])
        with np.nditer(arr, **opt) as iter:
            for elem in iter:
                item = elem.item()
                if isinstance(item, np.ndarray):
                    item = np.ndarray.view(item, object, np.ndarray)
                    if item.ndim == 0:
                        item = item.item()
                    else:
                        item = item.tolist()
                    elem[()] = item
                    rebuild = True
        if rebuild:
            # Recurse (we may have arrays of arrays of arrays...)
            return cls._unroll_build(arr.tolist())
        return arr

    @property
    def as_cell(self) -> "Cell":
        return self

    def deepcat(self, owndata=None) -> "Cell":
        """
        Convert a (nested) cell of cells into a deep cell array.
        """
        cls = type(self)
        copy = self._unroll_build(np.copy(self))
        copy = np.ndarray.view(copy, cls)

        # take ownership
        if owndata:
            tmp = copy
            copy = cls(tmp.shape, strides=tmp.strides)
            copy[...] = tmp

        return copy

    def __call__(self, *index):
        # We should only use this syntax when accessing elements into an
        # implictely created cell. In that context, we can just defer to
        # square bracket indexing. The point of using round brackets is
        # simply to instruct a DelayedArray that it should transform itself
        # into a Cell.
        #
        # NOTES:
        #
        #   1. We could implement round brackets only in DelayedArrays,
        #      but I like the symmetry of having them in CellArrays too.
        #      It enables things like
        #      ```python
        #      a.b(0).c = 'd'  # Instructs that b is a Cell
        #      a.b(1).c = 'e'  # At this point b is already a Cell,
        #                      # but it's nicer to use the same syntax as above
        #      ```
        #
        #   2. This implementation means that using round brackets for
        #      *accessing* data slices (`b(slice(2))`) does not have the
        #      same behaviour as in matlab (`b{1:2}`). This is a very uncommon
        #      use case, though. And single element indexing does work as
        #      expected (python's `b(1)` == matlab's `b{2}`).
        #
        #   3. I substitute `slice` with `slice(None)` to make the syntax
        #      for slicing whole axes more compact.
        #
        index = tuple(slice(None) if idx is slice else idx for idx in index)
        return self[index]


# ----------------------------------------------------------------------
# Struct
# ----------------------------------------------------------------------


class _DictMixin(MutableMapping):

    # NOTE:
    #
    #   Making Struct inherit from MutableMapping is a bit hacky
    #   because only scalar Struct implement a proper mapping protocol.
    #   For non-scalar Struct arrays, iteration is over array elements
    #   (not keys), as are `__len__`, `__contains__`, `__eq__`, etc.
    #
    #   The only abstract methods from MutableMapping are:
    #   * __getitem__   -> implemented in Struct
    #   * __setitem__   -> implemented in Struct
    #   * __delitem__   -> implemented in Struct
    #   * __len__       -> !! double meaning, implemented here
    #   * __iter__      -> !! double meaning, implemented here
    #
    #   MutableSequence implements the following non-abstract methods,
    #   but we overload them for speed:
    #   * __contains__  -> !! double meaning
    #   * __eq__        -> !! double meaning -> implemented in np.ndarray
    #   * __ne__        -> !! double meaning -> implemented in np.ndarray
    #   * keys          -> implemented here
    #   * items         -> implemented here
    #   * values        -> implemented here
    #   * get           -> implemented in Struct
    #   * pop           -> implemented in Struct
    #   * popitem       -> implemented in Struct
    #   * clear         -> implemented in Struct
    #   * update        -> implemented in Struct
    #   * setdefault    -> implemented in Struct

    # --- views --------------------------------------------------------
    class KeysView(KeysView):

        def __init__(self, parent):
            self._parent = parent

        def __len__(self):
            return len(self._parent._allkeys())

        def __iter__(self):
            return iter(self._parent._allkeys())

        def __contains__(self, key):
            return key in self._parent._allkeys()

        def __repr__(self):
            return f"dict_keys({list(self)})"

        __str__ = __repr__

    class ValuesView(ValuesView):

        def __init__(self, parent):
            self._parent = parent

        def __len__(self):
            return len(self._parent.as_dict().values())

        def __iter__(self):
            return iter(self._parent.as_dict().values())

        def __contains__(self, value):
            return value in self._parent.as_dict().values()

        def __repr__(self):
            return f"dict_values({list(self)})"

        __str__ = __repr__

    class ItemsView(ItemsView):

        def __init__(self, parent):
            self._parent = parent

        def __len__(self):
            return len(self._parent.as_dict().items())

        def __iter__(self):
            return iter(self._parent.as_dict().items())

        def __contains__(self, item):
            return item in self._parent.as_dict().items()

        def __repr__(self):
            return f"dict_items({list(self)})"

        __str__ = __repr__

    # --- magic --------------------------------------------------------

    def __len__(self):
        if self.ndim:
            return np.ndarray.__len__(self)
        else:
            return len(self.keys())

    def __contains__(self, key):
        if self.ndim:
            return np.ndarray.__contains__(self, key)
        else:
            return key in self.keys()

    def __iter__(self):
        if self.ndim:
            return np.ndarray.__iter__(self)
        else:
            return iter(self.keys())

    def __getitem__(self, key):
        if key in self.keys():

            # NOTE
            #   If some of the dictionaries in the array do not have
            #   their field `key` properly set, we assign an empty
            #   numeric array (same default value as in matlab).

            arr = np.ndarray.view(self, np.ndarray)
            opt = dict(flags=['refs_ok', 'zerosize_ok'], op_flags=['readonly'])
            with np.nditer(arr, **opt) as iter:
                for elem in iter:
                    elem.item().setdefault(key, _empty_array())

            # NOTE
            #   We then defer to `as_dict`

            return self.as_dict(keys=[key])[key]

        else:

            # NOTE
            #   We return a new (delayed) struct, whose elements under
            #  `key` are delayed arrays that point to `self` (and *not*
            #   to the delayed struct). This way, when the objects
            #   implicitely assigned to `key` get finalized, they are
            #   inserted into the orginal struct (`self`), not into
            #   the delayed struct (`delayed`).
            #
            #   We do not need to use a `DelayedStruct` here.

            parent = getattr(self, "_delayed_wrapper", self)

            delayed = Struct(self.shape)
            opt = dict(
                flags=['refs_ok', 'zerosize_ok', 'multi_index'],
                op_flags=['writeonly', 'no_broadcast']
            )
            arr = np.ndarray.view(delayed, np.ndarray)
            with np.nditer(arr, **opt) as iter:
                for elem in iter:
                    item = elem.item()
                    item[key] = AnyDelayedArray(parent, iter.multi_index, key)

            return delayed.as_dict(keys=[key])[key]

    def __setitem__(self, key, value):
        arr = np.ndarray.view(self, np.ndarray)

        if np.ndim(arr) == 0:

            # Scalar array: assign value to the field
            if isinstance(value, self.deal):
                # `deal` objects are cells and cannot be 0-dim
                raise ValueError("Cannot broadcast.")
            arr.item()[key] = MatlabType.from_any(value)

        elif isinstance(value, self.deal):

            # Each element in the struct array is matched with an element
            # in the "deal" array.
            value = value.broadcast_to_struct(self)
            opt = dict(flags=['refs_ok', 'zerosize_ok', 'multi_index'],
                       op_flags=['readonly'])
            with np.nditer(arr, **opt) as iter:
                for elem in iter:
                    val = value[iter.multi_index]
                    if isinstance(val, self.deal):
                        val = val.to_cell()
                    elem.item()[key] = MatlabType.from_any(val)

        else:

            # Assign the same value to all elements in the struct array.
            opt = dict(flags=['refs_ok', 'zerosize_ok'], op_flags=['readonly'])
            value = MatlabType.from_any(value)
            with np.nditer(arr, **opt) as iter:
                for elem in iter:
                    elem.item()[key] = value

    def __delitem__(self, key):
        if key not in self._allkeys():
            raise KeyError(key)
        arr = np.ndarray.view(self, np.ndarray)
        opt = dict(flags=['refs_ok', 'zerosize_ok'], op_flags=['readonly'])
        with np.nditer(arr, **opt) as iter:
            for elem in iter:
                del elem.item()[key]

    # --- mapping ------------------------------------------------------

    def keys(self):
        return self.KeysView(self)

    def items(self):
        return self.ItemsView(self)

    def values(self):
        return self.ValuesView(self)

    def setdefault(self, key, value=None):
        arr = np.ndarray.view(self, np.ndarray)
        opt = dict(flags=['refs_ok', 'zerosize_ok'], op_flags=['readonly'])
        with np.nditer(arr, **opt) as iter:
            for elem in iter:
                item = elem.item()
                if value is None:
                    value = _empty_array()
                else:
                    value = MatlabType.from_any(value)
                item.setdefault(key, value)

    def update(self, other):
        other = Struct.from_any(other)
        other = np.ndarray.view(other, np.ndarray)
        other = np.broadcast_to(other, self.shape)

        arr = np.ndarray.view(self, np.ndarray)
        opt = dict(flags=['refs_ok', 'zerosize_ok', 'multi_index'],
                   op_flags=['readonly'])
        with np.nditer(arr, **opt) as iter:
            for elem in iter:
                other_elem = other[iter.multi_index]
                item = elem.item()
                item.update(other_elem)

    # --- helper ------------------------------------------------------

    class deal(Cell):
        """
        Helper class to assign values into a specific field of a Struct array.

        ```python
        s = Struct(2)
        s.field = [1, 2]
        print(s)
        # [{"field": [1, 2]}, {"field": [1, 2]}]

        s = Struct(2)
        s.field = Struct.deal([1, 2])
        print(s)
        # [{"field": 1}, {"field": 2}]
        ```
        """
        # The idea is to have a type that tells Struct.__setattr__
        # that we want to broadcast the object before assigning it to
        # the field. We let the target struct tell this object which
        # field is being assigned and this object transforms itself
        # into a struct array with a single field (but multiple elements).
        # We can then let broadcasting do its magic.

        def __new__(cls, arg, **kwargs):
            return cls.from_any(arg, **kwargs)

        def broadcast_to_struct(self, struct: "Struct") -> "Struct.deal":
            shape = struct.shape + self.shape[len(struct.shape):]
            return np.broadcast_to(self, shape)

        def to_cell(self) -> "Cell":
            return np.ndarray.view(self, Cell)


class Struct(_DictMixin, WrappedArray):
    """
    Struct array, compatible with matlab structs.

    ```python
    # Instantiate from size
    Struct(N, M, ...)
    Struct([N, M, ...])
    Struct.from_shape([N, M, ...])

    # Instantiate from existing struct array
    # (or list/cell of dictionaries)
    Struct(struct_like)
    Struct.from_any(struct_like)

    # Instantiate from dictionary
    Struct(a=x, b=y)
    Struct({"a": x, "b": y})
    Struct.from_any({"a": x, "b": y})
    ```

    The following field names correspond to existing attributes or
    methods of `Struct` objects and are therefore protected. They can
    still be used as field names, but only through the dictionary syntax
    (`s["shape"]`), not the dot syntax (`s.shape`):

    * `ndim -> int`            : number of dimensions
    * `shape -> list[int]`     : array shape
    * `size -> int`            : number of elements
    * `reshape() -> Struct`    : struct array with a different shape
    * `keys() -> list[str]`    : field names
    * `values() -> list`       : values (per key)
    * `items() -> [str, list]` : (key, value) pairs
    * `get() -> list`          : value (per element)
    * `setdefault()`           : sets default value for field name
    * `update()`               : update fields from dictionary-like
    * `as_num -> raise`        : interpret object as a numeric array
    * `as_cell -> raise`       : interpret object as a cell array
    * `as_struct -> Struct`    : interpret object as a struct array
    * `as_dict() -> dict`      : convert to plain dictionary
    * `from_shape() -> Struct` : build a new empty struct
    * `from_any() -> Struct`   : build a new struct by (shallow) copy
    * `from_cell() -> Struct`  : build a new struct by (shallow) copy

    The following field names are protected because they have a special
    meaning in the python language. They can still be used as field names
    through the dictionary syntax:
    `as`        `assert`    `break`     `class`     `continue`  `def`
    `del`       `elif`      `else`      `except`    `False`     `finally`
    `for`       `from`      `global`    `if`        `import`    `in`
    `is`        `lambda`    `None`      `nonlocal`  `not`       `or`
    `pass`      `raise`     `return`    `True`      `try`       `while`
    `with`      `yield`
    """

    # NOTE
    #   _DictMixin must have precedence over _WrappedArray so that its
    #   method overload those from np.ndarray. This is why the
    #   inheritence order is (_DictMixin, _WrappedArray).

    # List of public attributes and methods from the ndarray class that
    # we keep in Struct. I've tried to find the minimal set of attributes
    # required to not break the numpy api.
    _NDARRAY_ATTRS = ("ndim", "shape", "size", "reshape")

    _DelayedType = DelayedStruct

    @classmethod
    def _DEFAULT(self, shape: list = ()) -> np.ndarray:
        # if len(shape) == 0:
        #     out = np.array(None)
        #     out[()] = dict()
        #     return out

        data = np.empty(shape, dtype=dict)
        opt = dict(
            flags=['refs_ok', 'zerosize_ok'],
            op_flags=['writeonly', 'no_broadcast']
        )
        with np.nditer(data, **opt) as iter:
            for elem in iter:
                elem[()] = dict()
        return data

    def _fill_default(self):
        arr = np.ndarray.view(self, np.ndarray)
        flags = dict(flags=['refs_ok', 'zerosize_ok'], op_flags=['readwrite'])
        with np.nditer(arr, **flags) as iter:
            for elem in iter:
                elem[()] = dict()
        return self

    def __new__(cls, *args, **kwargs) -> "Struct":
        kwargs["__has_dtype"] = False
        kwargs["__has_order"] = False
        mode, arg, kwargs = cls._parse_args(*args, **kwargs)
        if mode == "shape":
            obj = super().__new__(cls, shape=arg, dtype=dict)._fill_default()
        else:
            obj = cls.from_any(arg)
        obj.update(kwargs)
        return obj

    def _as_runtime(self) -> dict:
        if self.ndim == 0:
            data = np.ndarray.view(self, np.ndarray).item()
            data = MatlabType._to_runtime(data)
            return data

        size = np.array([[*np.shape(self)]])
        data = np.ndarray.view(self, np.ndarray)
        data = np.reshape(data, [-1], order="F")
        data = MatlabType._to_runtime(data)
        return dict(type__='structarray', size__=size, data__=data)

    @classmethod
    def _from_runtime(cls, objdict: dict) -> "Struct":
        if objdict['type__'] != 'structarray':
            raise TypeError('objdict is not a structarray')
        size = np.array(objdict['size__'], dtype=np.uint64).ravel()
        if len(size) == 2 and size[0] == 1:
            # NOTE: should not be needed for Cell, as this should
            # have been taken care of by MPython, but I am keeping it
            # here for symmetry with Array and Struct.
            size = size[1:]
        data = np.array(objdict['data__'], dtype=object)
        data = data.reshape(size)
        try:
            obj = data.view(cls)
        except Exception:
            raise RuntimeError(
                f'Failed to construct Struct data:\n'
                f'  data={data}\n'
                f'  objdict={objdict}'
            )

        # recurse
        opt = dict(flags=['refs_ok', 'zerosize_ok'],
                   op_flags=['readonly', 'no_broadcast'])
        with np.nditer(data, **opt) as iter:
            for elem in iter:
                item = elem.item()
                for key, val in item.items():
                    item[key] = MatlabType._from_runtime(val)

        return obj

    @classmethod
    def from_shape(cls, shape=tuple(), **kwargs) -> "Struct":
        """
        Build a struct array of a given size.

        Parameters
        ----------
        shape : list[int]
            Input shape.

        Other Parameters
        ----------------
        order : {"C", "F"} | None, default="C"
            Memory layout.
            * "C" row-major (C-style);
            * "F" column-major (Fortran-style).

        Returns
        -------
        struct : Struct
            New struct array.

        """
        return cls(list(shape), **kwargs)

    @classmethod
    def from_any(cls, other, **kwargs) -> "Struct":
        """
        * Convert a dict-like object to struct; or
        * Convert an array of dict-like objects to a struct array.

        Parameters
        ----------
        other : DictLike | ArrayLike[DictLike]
            object to convert.

        Other Parameters
        ----------------
        order : {"C", "F", "A", "K"} | None, default=None
            Memory layout.
            * "C" row-major (C-style);
            * "F" column-major (Fortran-style);
            * "A" (any) means "F" if a is Fortran contiguous, "C" otherwise;
            * "K" (keep) preserve input order;
            * `None` preserve input order if possible, "C" otherwise.
        copy : bool | None, default=None
            Whether to copy the underlying data.
            * `True` : the object is copied;
            * `None` : the the object is copied only if needed;
            * `False`: raises a `ValueError` if a copy cannot be avoided.
        owndata : bool, default=None
            If True, ensures that the returned Struct owns its data.
            This may trigger an additional copy.

        Returns
        -------
        struct : Struct
            Converted structure.
        """
        if isinstance(other, dict) and "type__" in other:
            # matlab object
            return cls._from_runtime(other)

        kwargs["dtype"] = dict

        # prepare for copy
        owndata = kwargs.pop("owndata", False)
        copy = None if owndata else kwargs.pop("copy", None)
        inp = other

        # convert to array[dict]
        other = np.asanyarray(other, **kwargs)
        other = cls._unroll_build(other)

        # check all items are dictionaries
        arr = np.ndarray.view(other, np.ndarray)
        opt = dict(flags=['refs_ok', 'zerosize_ok'], op_flags=['readonly'])
        with np.nditer(arr, **opt) as iter:
            if not all(isinstance(elem.item(), dict) for elem in iter):
                raise TypeError("Not an array of dictionaries")

        # view as Struct
        other = np.ndarray.view(other, cls)

        # copy (after view so that output owns data if copy=True)
        other = _copy_if_needed(other, inp, copy)

        # take ownership
        if owndata:
            tmp = other
            other = cls(tmp.shape, dtype=tmp.dtype, strides=tmp.strides)
            other[...] = tmp

        # nested from_any
        opt = dict(flags=['refs_ok', 'zerosize_ok'], op_flags=['readonly'])
        with np.nditer(other, **opt) as iter:
            for elem in iter:
                item: dict = elem.item()
                for k, v in item.items():
                    item[k] = MatlabType.from_any(v)

        return other

    @classmethod
    def from_cell(cls, other, **kwargs) -> "Struct":
        """See `from_any`."""
        if not isinstance(other, Cell):
            raise TypeError(f"Expected a {Cell} but got a {type(other)}.")
        return cls.from_any(other, **kwargs)

    @classmethod
    def _unroll_build(cls, other):
        # The logic here is that we may sometimes end up with arrays of
        # arrays of dict rather than a single deep array[dict]
        # (for example when converting cells of cells of dict).
        # To circumvent this, we find elements that are arrays, convert
        # them to lists, and recurse.
        rebuild = False
        arr = np.ndarray.view(other, np.ndarray)
        flags = dict(flags=['refs_ok', 'zerosize_ok'], op_flags=['readwrite'])
        with np.nditer(arr, **flags) as iter:
            for elem in iter:
                item = elem.item()
                if isinstance(item, np.ndarray):
                    item = np.ndarray.view(item, dict, np.ndarray)
                    if item.ndim == 0:
                        item = item.item()
                    else:
                        item = item.tolist()
                    elem[()] = item
                    rebuild = True
        if rebuild:
            # Recurse (we may have arrays of arrays of arrays...)
            return cls._unroll_build(other)
        return other

    @property
    def as_struct(self) -> "Struct":
        return self

    def __repr__(self):
        if self.ndim == 0:
            # Scalar struct -> display as a dict
            return repr(np.ndarray.view(self, np.ndarray).item())
        else:
            return super().__repr__()

    def as_dict(self, keys=None) -> dict:
        """
        Convert the object into a plain dict.

        * If a struct, return the underlying dict (no copy, is a view)
        * If a struct array, return a dict of Cell (copy, not a view)
        """
        self._ensure_defaults_are_set(keys)

        # NOTE
        #   The `keys` argument is only used in `__getattr__` to avoid
        #   building the entire dictionary, when the content of a single
        #   key is eventually used.

        # scalar struct -> return the underlying dictionary
        arr = np.ndarray.view(self, np.ndarray)

        if arr.ndim == 0:
            asdict = arr.item()
            if keys is not None:
                asdict = {key: asdict[key] for key in keys}
            return asdict

        # otherwise     -> reverse array/dict order -> dict of cells of values

        if keys is None:
            keys = self._allkeys()
        elif isinstance(keys, str):
            keys = [keys]

        opt = dict(flags=['refs_ok', 'zerosize_ok'], op_flags=['readwrite'])
        asdict = {key: [] for key in keys}
        with np.nditer(arr, **opt) as iter:
            for elem in iter:
                item = elem.item()
                for key in keys:
                    asdict[key].append(item[key])
        for key in keys:
            asdict[key] = Cell.from_any(asdict[key])
        raise ValueError(keys)
        return asdict

    def _allkeys(self):
        # Return all keys present across all elements.
        # Keys are ordered by (1) element (2) within-element order
        mock = {}
        arr = np.ndarray.view(self, np.ndarray)
        opt = dict(flags=['refs_ok', 'zerosize_ok'], op_flags=['readonly'])
        with np.nditer(arr, **opt) as iter:
            for elem in iter:
                mock.update({key: None for key in elem.item().keys()})
        return mock.keys()

    def _ensure_defaults_are_set(self, keys=None):
        """
        If a new key is set in an array element, this function ensures
        that all other elements are assigned a default value in the new key.
        """
        arr = np.ndarray.view(self, np.ndarray)

        if arr.ndim == 0:
            if keys:
                item: dict = arr.item()
                for key in keys:
                    item.setdefault(key, _empty_array())

        if keys is None:
            keys = self._allkeys()
        elif isinstance(keys, str):
            keys = [keys]

        opt = dict(flags=['refs_ok', 'zerosize_ok'], op_flags=['readonly'])
        with np.nditer(arr, **opt) as iter:
            for elem in iter:
                item: dict = elem.item()
                for key in keys:
                    item.setdefault(key, _empty_array())

    # --------------
    # Bracket syntax
    # --------------

    def __getitem__(self, index):
        if isinstance(index, str):
            try:
                return getattr(self, index)
            except AttributeError as e:
                raise KeyError(str(e))
        else:
            obj = WrappedArray.__getitem__(self, index)
            if not isinstance(obj, (Struct, DelayedStruct)):
                # We've indexed a single element, but we do not want
                # to expose the underlying dictionary. Instead,
                # we return an empty-sized view of the element, which
                # is still of type `Struct`.
                if not isinstance(index, tuple):
                    index = (index,)
                index += (None,)
                obj = np.ndarray.__getitem__(self, index)
                obj = np.reshape(obj, [])
            return obj

    def __setitem__(self, index, value):
        value = MatlabType.from_any(value)
        if isinstance(index, str):
            setattr(self, index, value)
        else:
            WrappedArray.__setitem__(self, index, value)
        self._ensure_defaults_are_set()

    def __delitem__(self, index):
        if isinstance(index, str):
            try:
                return delattr(self, index)
            except AttributeError as e:
                raise KeyError(str(e))
        return WrappedArray.__delitem__(self, index)

    # ----------
    # Dot syntax
    # ----------

    def __getattribute__(self, key):
        # Hide public numpy attributes
        asnumpy = np.ndarray.view(self, np.ndarray)
        if (
            hasattr(asnumpy, key) and key[:1] != "_" and
            key not in type(self)._NDARRAY_ATTRS
        ):
            raise AttributeError(f"hide numpy.ndarray.{key}")
        return super().__getattribute__(key)

    def __getattr__(self, key):
        if key[:1] == "_":
            raise AttributeError(
                f"{type(self).__name__} object has no attribute '{key}'"
            )
        try:
            return _DictMixin.__getitem__(self, key)
        except KeyError as e:
            raise AttributeError(str(e))

    def __setattr__(self, key, value):
        if key[:1] == "_":
            super().__setattr__(key, value)
            self._ensure_defaults_are_set()
            return
        try:
            _DictMixin.__setitem__(self, key, value)
            self._ensure_defaults_are_set()
            return
        except KeyError as e:
            raise AttributeError(str(e))

    def __delattr__(self, key):
        if key[:1] == "_":
            return super().__delattr__(key)
        try:
            return _DictMixin.__delitem__(self, key)
        except KeyError as e:
            raise AttributeError(str(e))


# ----------------------------------------------------------------------
# Object
# ----------------------------------------------------------------------


class MatlabClass(MatlabType):
    # FIXME: Can we rename this to `MatlabClass`?

    _subclasses = dict()

    def __new__(cls, *args, _objdict=None, **kwargs):
        if _objdict is None:
            if cls.__name__ in MatlabClass._subclasses.keys():
                obj = Runtime.call(cls.__name__, *args, **kwargs)
            else:
                obj = super().__new__(cls)
        else:
            obj = super().__new__(cls)
            obj._objdict = _objdict
        return obj

    def __init_subclass__(cls):
        super().__init_subclass__()
        if hasattr(cls, 'subsref'):
            cls.__getitem__ = MatlabClass.__getitem
            cls.__call__ = MatlabClass.__call

        if hasattr(cls, 'subsasgn'):
            cls.__setitem__ = MatlabClass.__setitem

        MatlabClass._subclasses[cls.__name__] = cls

    @classmethod
    def from_any(cls, other) -> "Array":
        if isinstance(other, dict) and "type__" in other:
            return cls._from_runtime(other)
        if not isinstance(other, cls):
            raise TypeError(f"Cannot convert {type(other)} to {cls}")
        return other

    @classmethod
    def _from_runtime(cls, objdict):
        if objdict['class__'] in MatlabClass._subclasses.keys():
            obj = MatlabClass._subclasses[objdict['class__']](
                _objdict=objdict
            )
        else:
            warnings.warn(f'Unknown Matlab class type: {objdict["class__"]}')
            obj = MatlabClass(_objdict=objdict)
        return obj

    def _as_runtime(self):
        return self._objdict

    def __getattr(self, key):
        try:
            return self.subsref({'type': '.', 'subs': key})
        except Exception:
            raise AttributeError(key)

    def __getitem(self, ind):
        index = self._process_index(ind)
        try:
            return self.subsref({'type': '()', 'subs': index})
        except Exception:
            ...
        try:
            return self.subsref({'type': '{}', 'subs': index})
        except Exception:
            raise IndexError(index)

    def __setitem(self, ind, value):
        index = self._process_index(ind)
        try:
            return self.subsasgn({'type': '()', 'subs': index}, value)
        except Exception:
            ...
        try:
            return self.subsasgn({'type': '{}', 'subs': index}, value)
        except Exception:
            raise IndexError(index)

    def __call(self, *index):
        index = self._process_index(index)
        try:
            return self.subsref({'type': '{}', 'subs': index})
        except Exception:
            raise IndexError(index)

    def _process_index(self, ind, k=1, n=1):
        try:
            return tuple(
                self._process_index(i, k+1, len(ind))
                for k, i in enumerate(ind)
            )
        except TypeError:
            pass

        if not hasattr(self, '__endfn'):
            self.__endfn = Runtime.call('str2func', 'end')

        def end():
            return Runtime.call(self.__endfn, self._as_runtime(), k, n)

        if isinstance(ind, int):
            if ind >= 0:
                index = ind + 1
            elif ind == -1:
                index = end()
            else:
                index = end() + ind - 1
        elif isinstance(ind, slice):
            if ind.start is None and ind.stop is None and ind.step is None:
                index = ':'
            else:
                if ind.start is None:
                    start = 1
                elif ind.start < 0:
                    start = end() + ind.start
                else:
                    start = ind.start + 1

                if ind.stop is None:
                    stop = end()
                elif ind.stop < 0:
                    stop = end() + ind.stop
                else:
                    stop = ind.stop + 1

                if ind.step is None:
                    step = 1
                else:
                    step = ind.step

                min_ = min(start, stop)
                max_ = max(start, stop)
                if step > 0:
                    index = np.arange(min_, max_, step)
                else:
                    index = np.arange(max_, min_, step)
        else:
            index = ind

        return index
