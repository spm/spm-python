import warnings
import numpy as np
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


_NP_VERSION = tuple(map(int, np.__version__.split(".")[:2]))
_NP_HAS_COPY = not (_NP_VERSION < (2, 1))


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
    _import_matlab()
    global matlab
    if matlab:
        return {
            matlab.double:  np.float64,
            matlab.single:  np.float32,
            matlab.logical: np.bool,
            matlab.uint64:  np.uint64,
            matlab.uint32:  np.uint32,
            matlab.uint16:  np.uint16,
            matlab.uint8:   np.uint8,
            matlab.int64:   np.int64,
            matlab.int32:   np.int32,
            matlab.int16:   np.int16,
            matlab.int8:    np.int8,
        }
    else:
        return {}


# ----------------------------------------------------------------------
# Types
# ----------------------------------------------------------------------


class MatlabType(object):
    """Generic type for objects that have an exact matlab equivalent."""

    @classmethod
    def from_any(cls, other):
        """
        Convert python objects to `MatlabType` objects
        (`Cell`, `Struct`, `Array`, `MatlabClassWrapper`).

        !!! warning "Conversion is performed in-place when possible."
        """
        # - we do not convert to matlab's own array types
        #   (`matlab.double`, etc);
        # - we do not convert to types that can be passed directly to
        #   the matlab runtime;
        # - instead, we convert to python types that mimic matlab types.
        if isinstance(other, MatlabType):
            if hasattr(other, "_finalize"):
                other = other._finalize()
            return other.from_any(other)  # nested call

        if isinstance(other, dict):
            if "type__" in other:
                type__ = other["type__"]

                if type__ == "structarray":
                    # Matlab returns a list of dictionaries in data__
                    # and the array shape in size__.
                    return Struct._from_runtime(other)

                elif type__ == "cell":
                    # Matlab returns a list of dictionaries in data__
                    # and the array shape in size__.
                    return Cell._from_runtime(other)

                elif type__ == "object":
                    # Matlab returns the object's fields serialized
                    # in a dictionary.
                    return MatlabClassWrapper._from_runtime(other)

                elif type__ == "sparse":
                    # Matlab returns a dense version of the array in data__.
                    if sparse:
                        return SparseArray._from_runtime(other)
                    else:
                        data = np.asarray(other['data__'], dtype=np.double)
                        return data.view(Array)

                else:
                    raise ValueError("Don't know what to do with type", type__)

            else:
                return Struct.from_any(other)

        if isinstance(other, (list, tuple, set)):
            # nested tuples are cells of cells, not cell arrays
            return Cell.from_any(other)

        if isinstance(other, (np.ndarray, int, float, complex, bool)):
            return Array.from_any(other)

        if isinstance(other, str):
            return other

        if other is None:
            # This can happen when matlab code is called without `nargout`
            return other

        if not matlab:
            _import_matlab()

        if matlab and isinstance(other, matlab.object):
            return MatlabFunction.from_any(other)

        if type(other) in _matlab_array_types():
            dtype = _matlab_array_types()[type(other)]
            return Array.from_any(other, dtype=dtype)

        raise TypeError(
            f"Cannot convert {type(other).__name__} into a matlab object."
        )

    @classmethod
    def _to_runtime(cls, obj):
        """
        Convert object to representation that the matlab runtime understand.
        """
        to_runtime = cls._to_runtime

        if isinstance(obj, MatlabType):
            # class / structarray / cell
            return obj._as_runtime()

        elif isinstance(obj, (list, tuple, set)):
            return type(obj)(map(to_runtime, obj))

        elif isinstance(obj, dict):
            return type(obj)(zip(obj.keys(), map(to_runtime, obj.values())))

        elif isinstance(obj, np.ndarray):
            obj = np.asarray(obj)
            if obj.dtype in (object, dict):
                shape, dtype = obj.shape, obj.dtype
                obj = np.fromiter(map(to_runtime, obj.flat), dtype=dtype)
                obj = obj.reshape(shape)
                return obj.tolist()
            return obj

        elif sparse and isinstance(obj, sparse.coo_array):
            return dict(type__='sparse', data__=obj.todense())

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


class MatlabFunction(MatlabType):
    """Wrapper for matlab function handles."""

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

    @property
    def as_default(self):
        return self


# ----------------------------------------------------------------------
# DelayedArray
# ----------------------------------------------------------------------


class DelayedArray(AnyMatlabArray):
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

    def __init__(self, parent=None):
        super().__init__()
        self._parent = parent
        self._array = None

    def _finalize(self):
        if self._array is None:
            if self._parent is not None:
                self._array = self._parent._DEFAULT()
            else:
                self._array = Array.from_any([])
        return self._array

    def _check_finalized(self):
        if self._array is not None:
            raise ValueError(
                f"This DelayedArray has been finalized and should not "
                f"be used anymore. Instead, use "
                f"{type(self._array)} object @ {hex(id(self._array))}"
            )

    @property
    def as_cell(self) -> "Cell":
        self._check_finalized()
        self._array = Cell()
        if self._parent is not None:
            self._parent._finalize()
        return self._array

    @property
    def as_struct(self) -> "Struct":
        self._check_finalized()
        self._array = Struct()
        if self._parent is not None:
            self._parent._finalize()
        return self._array

    @property
    def as_num(self) -> "Array":
        return self.__array__()

    as_default = as_num

    def __array__(self, dtype=None, copy=None):
        self._check_finalized()
        self._array = Array.from_any([], dtype=dtype)
        if self._parent is not None:
            self._parent._finalize()
        return self._array

    def __call__(self, *index):
        return self.as_cell(*index)

    def __getitem__(self, index):
        return self.as_struct[index]

    def __getattr__(self, key):
        if key in ("_array", "_parent"):
            # FIXME: this case should have been caught by __getattribute__
            # -> check if it is, or why it isn't.
            return super().__getattr__(key)
        return self.as_struct[key]

    def __setitem__(self, index, value):
        self._check_finalized()
        if isinstance(value, (dict, Struct)):
            array = self.as_struct
        elif isinstance(value, (tuple, Cell)):
            array = self.as_cell
            if isinstance(value, tuple):
                value = Cell.from_iterable(value)
        else:
            array = self.as_num
        array[index] = value

    def __setattr__(self, key, value):
        if key in ("_array", "_parent"):
            return super().__setattr__(key, value)
        self.as_struct[key] = value


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

    # Value used for delayed arrays whose type cannot be guessed
    # Must be implemented in Array/Cell/Struct.
    @classmethod
    def _DEFAULT(cls, n: list = ()):
        raise NotImplementedError

    # Value used to fill-in a newly allocated array.
    # Must be implemented in Array/Cell/Struct.
    def _DELAYED(self, n: list = ()):
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
            self._resize_for_index(index, mode="delayed")
            return super().__getitem__(index)

    def __setitem__(self, index, value):
        """Resize array if needed, then fallback to np.ndarray indexing."""
        value = MatlabType.from_any(value)
        try:
            return super().__setitem__(index, value)
        except IndexError:
            self._resize_for_index(index, mode="default")
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

    def _resize_for_index(self, index, mode="delayed"):
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
            elif not isinstance(next_index, slice):
                raise TypeError(
                    "Can only automatically resize cell if simple "
                    "indexing (int, slice) is used."
                )
            new_index.append(next_index)
            new_shape.append(next_shape)
        new_shape = new_shape + shape
        view_index = tuple(slice(x, None) for x in np.shape(self))
        np.ndarray.resize(self, new_shape, refcheck=False)
        arr = np.ndarray.view(self, np.ndarray)
        view_shape = arr[view_index].shape
        FILLER = self._DELAYED if mode == "delayed" else self._DEFAULT
        new_data = FILLER(view_shape)
        arr[view_index] = new_data

    def _finalize(self):
        """Transform all DelayedArrays into concrete arrays."""
        opt = dict(flags=['refs_ok', 'zerosize_ok'],
                   op_flags=['readwrite', 'no_broadcast'])
        with np.nditer(self, **opt) as iter:
            for elem in iter:
                item = elem.item()
                if isinstance(item, AnyMatlabArray):
                    # FIXME: this is done in MatlabType.from_any
                    # so get rid of this if/else and defer to from_any?
                    elem[()] = item._finalize()
                else:
                    elem[()] = MatlabType.from_any(item)
        return self


# ----------------------------------------------------------------------
# SparseArray
# ----------------------------------------------------------------------


if sparse:

    class WrappedSparseArray(sparse.sparray, AnyWrappedArray):
        """Base class for sparse arrays."""

        def to_dense(self) -> "Array":
            return Array.from_any(super().to_dense())

    class SparseArray(sparse.coo_array, WrappedSparseArray):
        """Matlab sparse arrays."""

        def __new__(cls, *args, **kwargs) -> "Array":
            mode, arg, kwargs = cls._parse_args(*args, **kwargs)
            if mode == "shape":
                return super().__new__(cls, shape=arg, **kwargs)
            else:
                if not isinstance(arg, (np.ndarray, sparse.sparray)):
                    arg = np.asanyarray(arg)
                return super().__new__(cls, arg, **kwargs)

        def _as_runtime(self) -> dict:
            data = super().todense()
            return dict(type__='sparse', data__=data)

        @classmethod
        def _from_runtime(cls, dictobj: dict) -> "SparseArray":
            if dictobj['type__'] != 'sparse':
                raise ValueError("Not a matlab sparse matrix")
            return cls.from_any(dictobj['data__'])

        @classmethod
        def from_shape(cls, shape=tuple(), **kwargs) -> "Array":
            """
            Build an array if a given shape.

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

        def _finalize(self):
            # Nothing to do, sparse array cannot contain python objects.
            return self


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
    Array(..., dtype=None, order=None, *, copy=None)
    ```
    """
    @classmethod
    def _DEFAULT(cls, n: list = ()) -> int:
        return 0

    def _DELAYED(self, n: list = ()) -> int:
        return 0

    def __new__(cls, *args, **kwargs) -> "Array":
        mode, arg, kwargs = cls._parse_args(*args, **kwargs)
        if mode == "shape":
            obj = super().__new__(cls, arg, **kwargs)
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
        return cls.from_any(other)

    @classmethod
    def from_shape(cls, shape=tuple(), **kwargs) -> "Array":
        """
        Build an array if a given shape.

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
        owndata : bool, default=False
            If True, ensures that the returned Struct owns its data.
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
        Convert a `Cell` ot a numeric `Array`.

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

    def _finalize(self):
        # Nothing to do, numeric array cannot contain python objects.
        return self


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
        other = Cell.from_any(other)
        return np.concatenate([self, other])

    def __radd__(self, other):
        other = Cell.from_any(other)
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

    def insert(self, index, object):
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
        self[index] = object

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
    Cell(..., order=None, *, copy=None, deepcat=False)
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
    """

    # NOTE
    #   _ListMixin must have precedence over _WrappedArray so that its
    #   method overload those from np.ndarray. This is why the
    #   inheritence order is (_ListMixin, _WrappedArray).

    @classmethod
    def _DEFAULT(cls, n: list = ()) -> np.ndarray:
        if len(n) == 0:
            return Array.from_any([])

        data = np.empty(n, dtype=object)
        opt = dict(
            flags=['refs_ok', 'zerosize_ok'],
            op_flags=['writeonly', 'no_broadcast']
        )
        with np.nditer(data, **opt) as iter:
            for elem in iter:
                elem[()] = Array.from_any([])
        return data

    def _DELAYED(self, n: list = ()) -> np.ndarray:
        if len(n) == 0:
            return DelayedArray(self)

        data = np.empty(n, dtype=object)
        opt = dict(
            flags=['refs_ok', 'zerosize_ok'],
            op_flags=['writeonly', 'no_broadcast']
        )
        with np.nditer(data, **opt) as iter:
            for elem in iter:
                elem[()] = DelayedArray(self)
        return data

    def _fill_default(self):
        arr = np.ndarray.view(self, np.ndarray)
        opt = dict(flags=['refs_ok', 'zerosize_ok'],
                   op_flags=['writeonly', 'no_broadcast'])
        with np.nditer(arr, **opt) as iter:
            for elem in iter:
                elem[()] = self._DEFAULT()
        return self

    def __new__(cls, *args, **kwargs) -> "Cell":
        mode, arg, kwargs = cls._parse_args(*args, **kwargs)
        kwargs["dtype"] = object
        if mode == "shape":
            if len(arg) == 0:
                # Scalar cells are forbidden
                arg = [0]
            return super().__new__(cls, arg, **kwargs)._fill_default()
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
        if objdict['type__'] != 'cell':
            raise TypeError('objdict is not a cell')
        size = np.array(objdict['size__'], dtype=np.uint32).ravel()
        data = np.array(objdict['data__'], dtype=object)
        data = data.reshape(size[::-1]).transpose()
        try:
            obj = data.view(cls)
        except Exception:
            raise RuntimeError(
                f'Failed to construct Cell data:\n'
                f'  data={data}\n'
                f'  objdict={objdict}'
            )
        return MatlabType.from_any(obj)

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
            If True, ensures that the returned Struct owns its data.
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

            def asrecursive(other):
                if isinstance(other, np.ndarray):
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

    def deepcat(self) -> "Cell":
        """
        Convert a (nested) cell of cells into a deep cell array.
        """
        cls = type(self)
        self = self._unroll_build(np.copy(self))
        self = np.ndarray.view(self, cls)
        return self

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
        # NOTE
        #   We only insert a DelayedArray if it is a completely new key.
        #   Otherwise the default value is [], as per matlab.
        isnewkey = key not in self.keys()
        arr = np.ndarray.view(self, np.ndarray)
        opt = dict(flags=['refs_ok', 'zerosize_ok'], op_flags=['readonly'])
        with np.nditer(arr, **opt) as iter:
            for elem in iter:
                elem.item().setdefault(
                    key,
                    DelayedArray(self) if isnewkey else Array.from_any([])
                )
        return self.as_dict()[key]

    def __setitem__(self, key, value):
        arr = np.ndarray.view(self, np.ndarray)

        if np.ndim(arr) == 0:
            # Scalar array: assign value to the field
            if isinstance(value, self.unpack):
                # unpacks are cells and cannot be 0-dim
                raise ValueError("Cannot broadcast.")
            arr.item()[key] = MatlabType.from_any(value)

        elif isinstance(value, self.unpack):
            # Each element in the struct array is matched with an element
            # in the "unpack" array.
            value = value.broadcast_to_struct(self)
            opt = dict(flags=['refs_ok', 'zerosize_ok', 'multi_index'],
                       op_flags=['readonly'])
            with np.nditer(arr, **opt) as iter:
                for elem in iter:
                    val = value[iter.multi_index]
                    if isinstance(val, self.unpack):
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

    def setdefault(self, key, value):
        arr = np.ndarray.view(self, np.ndarray)
        opt = dict(flags=['refs_ok', 'zerosize_ok'], op_flags=['readonly'])
        with np.nditer(arr, **opt) as iter:
            for elem in iter:
                item = elem.item()
                item.setdefault(key, MatlabType.from_any(value))

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

    class unpack(Cell):
        """
        Helper class to assign values into a specific field of a Struct array.

        ```python
        s = Struct(2)
        s.field = [1, 2]
        print(s)
        # [{"field": [1, 2]}, {"field": [1, 2]}]

        s = Struct(2)
        s.field = Struct.unpack([1, 2])
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

        def broadcast_to_struct(self, struct: "Struct") -> "Struct.unpack":
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

    @classmethod
    def _DEFAULT(self, n: list = ()) -> np.ndarray:
        if len(n) == 0:
            return dict()

        data = np.empty(n, dtype=dict)
        opt = dict(
            flags=['refs_ok', 'zerosize_ok'],
            op_flags=['writeonly', 'no_broadcast']
        )
        with np.nditer(data, **opt) as iter:
            for elem in iter:
                elem[()] = dict()
        return data

    _DELAYED = _DEFAULT

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
            obj = super().__new__(cls, arg, dtype=dict)._fill_default()
        else:
            obj = cls.from_any(arg)
        obj.update(kwargs)
        return obj

    def _as_runtime(self) -> dict:
        size = np.array([[*np.shape(self)]])
        data = np.ndarray.view(self, np.ndarray)
        data = np.reshape(data, [-1], order="F")
        data = MatlabType._to_runtime(data)
        return dict(type__='structarray', size__=size, data__=data)

    @classmethod
    def _from_runtime(cls, objdict: dict) -> "Struct":
        if objdict['type__'] != 'structarray':
            raise TypeError('objdict is not a structarray')
        size = np.array(objdict['size__'], dtype=np.uint32).ravel()
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
        return MatlabType.from_any(obj)

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
        owndata : bool, default=False
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

    def as_dict(self) -> dict:
        """
        Convert the object into a plain dict.

        * If a struct, return the underlying dict (no copy, is a view)
        * If a struct array, return a dict of Cell (copy, not a view)
        """
        # scalar struct -> return the underlying dictionary
        # otherwise     -> reverse array/dict order -> dict of cells of values
        if np.ndim(self) == 0:
            return np.ndarray.item(self)
        arr = np.ndarray.view(self, np.ndarray)
        opt = dict(flags=['refs_ok', 'zerosize_ok'], op_flags=['readwrite'])
        with np.nditer(arr, **opt) as iter:
            return {
                key: Cell.from_any([
                    elem.item().get(key, self._DEFAULT()) for elem in iter
                ]).reshape(np.shape(self))
                for key in self._allkeys()
            }

    def _allkeys(self):
        # Return all keys present across all elements.
        # Keys are ordered by (1) element (2) within-element order
        mock = {}
        arr = np.ndarray.view(self, np.ndarray)
        opt = dict(flags=['refs_ok', 'zerosize_ok'], op_flags=['readwrite'])
        with np.nditer(arr, **opt) as iter:
            for elem in iter:
                mock.update({key: None for key in elem.item().keys()})
        return mock.keys()

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
            obj = np.ndarray.__getitem__(self, index)
            if not isinstance(obj, Struct):
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
            np.ndarray.__setitem__(self, index, value)

    def __delitem__(self, key):
        if isinstance(key, str):
            try:
                return delattr(self, key)
            except AttributeError as e:
                raise KeyError(str(e))
        return np.ndarray.__delitem__(self, key)

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
            raise AttributeError(f"Struct object has no attribute '{key}'")
        try:
            return _DictMixin.__getitem__(self, key)
        except KeyError as e:
            raise AttributeError(str(e))

    def __setattr__(self, key, value):
        if key[:1] == "_":
            return super().__setattr__(key, value)
        try:
            return _DictMixin.__setitem__(self, key, value)
        except KeyError as e:
            raise AttributeError(str(e))

    def __delattr__(self, key):
        if key[:1] == "_":
            return super().__delattr__(key)
        try:
            return _DictMixin.__delitem__(self, key)
        except KeyError as e:
            raise AttributeError(str(e))

    # -------
    # Delayed
    # -------

    def _finalize(self):
        arr = np.ndarray.view(self, np.ndarray)
        opt = dict(flags=['refs_ok', 'zerosize_ok'], op_flags=['readwrite'])
        with np.nditer(arr, **opt) as iter:
            for elem in iter:
                item = elem.item()
                if not isinstance(item, dict):
                    elem[()] = {}
                    continue
                for key, value in item.items():
                    if isinstance(value, AnyMatlabArray):
                        # FIXME: this is done in MatlabType.from_any
                        # so get rid of this if/else and defer to from_any?
                        item[key] = value._finalize()
                    else:
                        item[key] = MatlabType.from_any(item[key])
        return self


# ----------------------------------------------------------------------
# Object
# ----------------------------------------------------------------------


class MatlabClassWrapper(MatlabType):
    # FIXME: Can we rename this to `MatlabClass`?

    _subclasses = dict()

    def __new__(cls, *args, _objdict=None, **kwargs):
        if _objdict is None:
            if cls.__name__ in MatlabClassWrapper._subclasses.keys():
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
            cls.__getitem__ = MatlabClassWrapper.__getitem
            cls.__call__ = MatlabClassWrapper.__call

        if hasattr(cls, 'subsasgn'):
            cls.__setitem__ = MatlabClassWrapper.__setitem

        MatlabClassWrapper._subclasses[cls.__name__] = cls

    @classmethod
    def from_any(cls, other) -> "Array":
        if isinstance(other, dict) and "type__" in other:
            return cls._from_runtime(other)
        if not isinstance(other, cls):
            raise TypeError(f"Cannot convert {type(other)} to {cls}")
        return other

    @classmethod
    def _from_runtime(cls, objdict):
        if objdict['class__'] in MatlabClassWrapper._subclasses.keys():
            obj = MatlabClassWrapper._subclasses[objdict['class__']](
                _objdict=objdict
            )
        else:
            warnings.warn(f'Unknown Matlab class type: {objdict["class__"]}')
            obj = MatlabClassWrapper(_objdict=objdict)
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
