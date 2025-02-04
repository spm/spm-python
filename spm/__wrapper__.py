try:
    from spm._spm import initialize
except ImportError as e:
    import os
    installer_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '_spm',
        'resources',
        'RuntimeInstaller.install')
    print("Failed to import spm._spm. This can be due to a failure to find Matlab Runtime. "
          "Please verify that Matlab Runtime is installed and its path is set. "
          "See https://www.mathworks.com/help/compiler/mcr-path-settings-for-run-time-deployment.html for instructions"
          " on how to setup the path. If the issue persists, please open an issue with the entire error message at "
          "https://github.com/spm/spm-python/issues.")

    raise e

import warnings
import numpy as np
import matlab
import itertools

_matlab_numpy_types = {
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


# ----------------------------------------------------------------------
# Runtime
# ----------------------------------------------------------------------

class Runtime:
    _instance = None
    verbose = True

    @staticmethod
    def instance():
        if Runtime._instance is None:
            if Runtime.verbose:
                print('Initializing Matlab Runtime...')
            Runtime._instance = initialize()
        return Runtime._instance

    @staticmethod
    def call(fn, *args, **kwargs):
        (args, kwargs) = Runtime._process_argin(*args, **kwargs)
        res = Runtime.instance().mpython_endpoint(fn, *args, **kwargs)
        return Runtime._process_argout(res)

    # FIXME: this method is not used anymore -- delete it later
    # @staticmethod
    # def _cast_argin(arg):
    #     if isinstance(arg, (MatlabClassWrapper, OldStructArray)):
    #         arg = arg._as_matlab_object()
    #     if isinstance(arg, dict):
    #         _, arg = Runtime._process_argin(**arg)
    #     elif isinstance(arg, (tuple, list, set)):
    #         arg, _ = Runtime._process_argin(*arg)
    #     return arg

    @staticmethod
    def _process_argin(*args, **kwargs):
        args = tuple(map(_as_matlab_object, args))
        kwargs = dict(zip(
            kwargs.keys(),
            map(_as_matlab_object, kwargs.values())))

        return args, kwargs

    @staticmethod
    def _process_argout(res):
        return asmatlab(res)

        # FIXME: old version kept for discussion,
        #        now deferred to `asmatlab` -- delete it later
        #
        # out = res
        # if type(res) in _matlab_numpy_types.keys():
        #     try:
        #         out = np.asarray(res, dtype=_matlab_numpy_types[type(res)])
        #     except:
        #         pass
        # elif isinstance(res, tuple):
        #     out = tuple(Runtime._process_argout(r) for r in res)
        # elif isinstance(res, list):
        #     out = list(Runtime._process_argout(r) for r in res)
        # elif isinstance(res, OldStructArray):
        #     out = OldStructArray(Runtime._process_argout(r) for r in res)
        # elif isinstance(res, dict):
        #     res = dict(zip(res.keys(), map(Runtime._process_argout, res.values())))
        #     if 'type__' in res.keys():
        #         if res['type__'] == 'object':
        #             out = MatlabClassWrapper._from_matlab_object(res)
        #         elif res['type__'] == 'structarray':
        #             out = OldStructArray._from_matlab_object(res)
        #         elif res['type__'] == 'sparse':
        #             out = np.asarray(res['data__'], dtype=np.double)
        #         else:
        #             out = res
        #     else:
        #         out = OldStruct(**res)
        # return out


# ----------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------


def cell(*iterable):
    """
    Return a 1D `Cell` that contains the input elements.
    """
    # `Cell(tuple[cells])` may combine its input into a cell array.
    # This helper ensures that we only create a cell at the first level,
    # i.e., `cell(x, y, z)` is equivalent to matlab's `{x y z}`.
    #
    # We could also simply name is `c`, which matches R's `c(x, y, z)`,
    # and avoids confusion between `Cell` and `cell`.
    obj = Cell(len(iterable))
    for i, elem in enumerate(iterable):
        obj[i] = elem
    return obj


def num2cell(array):
    """
    Convert an `Array` to a `Cell`.
    """
    # TODO: expose matlab's `num2cell` in the spm bindings and check
    #       that the python and matlab's versions have equivalent bhv?
    obj = np.asanyarray(array, dtype=object)
    return np.ndarray.view(obj, Cell)


def cell2num(cell, dtype=None):
    """
    Convert a `Cell` to an `Array`.
    """
    # TODO: expose matlab's `cell2num` in the spm bindings and check
    #       that the python and matlab's versions have equivalent bhv?
    obj = np.asanyarray(cell.tolist(), dtype=dtype)
    return np.ndarray.view(obj, Array)


def struct2cell(struct):
    """
    Convert a `Struct` to a `Cell`.
    The output cell contains the struct's values (not the keys).
    """
    # TODO: expose matlab's `struct2cell` in the spm bindings and check
    #       that the python and matlab's versions have equivalent bhv?
    obj = np.stack([struct[key] for key in struct.keys()])
    return np.ndarray.view(obj, Cell)


def cell2struct(cell):
    """
    Convert a `Cell` of `Struct` into a `Struct`.
    """
    # TODO: expose matlab's `cell2struct` in the spm bindings and check
    #       that the python and matlab's versions have equivalent bhv?
    obj = np.empty(cell.shape, dtype=dict)
    for i, x in cell._iterall():
        obj[i] = x
    return np.ndarray.view(obj, Struct)


def ascell(other):
    """
    Convert (nested) list-like objects to cells.
    """
    other = np.asanyarray(other, dtype=object)
    return asmatlab(np.ndarray.view(other, Cell))


def asnum(other):
    """
    Convert array-like objects to numeric arrays.
    """
    other = np.asanyarray(other)
    if not issubclass(other.dtype.type, np.number):
        other = np.asanyarray(other, dtype=np.float64)
    return np.ndarray.view(other, Array)


def asstruct(other):
    """
    Convert (nested) dict-like objects to struct.
    Convert (array of) dict-like objects to struct array.
    """
    if isinstance(other, np.ndarray) and other.dtype in (object, dict):
        return asmatlab(np.ndarray.view(other, Struct))
    return asmatlab(Struct(other))


def asmatlab(other):
    """
    Convert python objects to matlab-like objects (`Cell`, `Struct`, `Array`).

    !!! warning "Conversion is performed in-place when possible."
    """
    # NOTE: `asmatlab` might be a misleading name:
    #   - we do not convert to matlab's own array types (`matlab.double`, etc);
    #   - we do not convert to types that can be passed directly to matlab's
    #     bindings;
    #   - instead, we convert to python types that mimic matlab types.
    #
    # Can we find another (less misleading) name?
    #   - `asspm` or `as_spm` ?
    #   - `asspmarray` or `as_spm_array` ?
    #   - `assmartarray` or `as_smart_array` ?
    if isinstance(other, Array):
        return other

    if isinstance(other, Cell):
        for i, x in other._iterall():
            np.ndarray.__setitem__(other, i, asmatlab(x))
        return other

    if isinstance(other, Struct):
        for i, x in other._iterall():
            for k, v in x.items():
                x[k] = asmatlab(v)
        return other

    if isinstance(other, dict):
        if "type__" in other:
            type__ = other["type__"]
            if type__ == "structarray":
                return Struct._from_matlab_object(other)
            elif type__ == 'object':
                return MatlabClassWrapper._from_matlab_object(other)
            elif type__ == 'sparse':
                return np.asarray(other['data__'], dtype=np.double).view(Array)
            else:
                raise ValueError("Don't know what to do with type", type__)
        else:
            return asstruct(other)

    if isinstance(other, (tuple, set)):
        return ascell(other)

    if isinstance(other, (list, np.ndarray, int, float, complex, bool)):
        try:
            return asnum(other)
        except (ValueError, TypeError):
            return ascell(other)

    if isinstance(other, _MatlabType):
        if hasattr(other, "_finalize"):
            return other._finalize()
        else:
            return other

    if isinstance(other, str):
        return other

    if other is None:
        # NOTE: This can happen when matlab code is called without `nargout`
        return other

    raise TypeError(
        f"Cannot convert {type(other).__name__} into a matlab object."
    )


def _as_matlab_object(obj):
    """
    Convert object to representation that the matlab bindings understand.
    """
    if hasattr(obj, "_as_matlab_object"):
        return obj._as_matlab_object()
    if isinstance(obj, (list, tuple, set)):
        return type(obj)(map(_as_matlab_object, obj))
    elif isinstance(obj, dict):
        return type(obj)(zip(obj.keys(), map(_as_matlab_object, obj.values())))
    elif isinstance(obj, np.ndarray):
        obj = np.asarray(obj)
        if obj.dtype in (object, dict):
            shape, dtype = obj.shape, obj.dtype
            obj = np.fromiter(map(_as_matlab_object, obj.flat), dtype=dtype)
            obj = obj.reshape(shape)
            return obj.tolist()
        return obj
        # TODO: what about sparse numpy arrays? Does matlab understand them?
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


class unpack(np.ndarray):
    """
    Helper class to assign values into a specific field of a non-scalar Struct.

    ```python
    s = Struct(2)
    s.field = cell(1, 2)
    print(s)
    # [{"field": [1, 2]}, {"field": [1, 2]}]

    s = Struct(2)
    s.field = unpack(1, 2)
    print(s)
    # [{"field": 1}, {"field": 2}]
    ```
    """
    # TODO:
    #   The idea is to have a type that tells Struct.__setattr__
    #   that we want to broadcast the object before assigning it to the field.
    #   I am not sure about the exact syntax yet, so I keep it simple for now.
    def __new__(cls, *args, **kwargs):
        raise NotImplementedError()
        return super().__new__(cls, *args, **kwargs)


# ----------------------------------------------------------------------
# Types
# ----------------------------------------------------------------------


class _MatlabType(object):
    """Generic type for all objects that have an exact matlab equivalent."""
    pass


class _MatlabClass(_MatlabType):
    """Base class for user-defined matlab classes."""
    # TODO: Can we use this name instead of `MatlabClassWrapper`?
    pass


class _MatlabArray(_MatlabType):
    """Base class for all matlab-like arrays (numeric, cell, struct)."""
    pass


class _DelayedArray(_MatlabArray):
    """
    This is an object that we return when we don't know how an indexed element
    will be used yet.

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
        * a `Struct` (in all "get" cases, and in the "set" context
          `a[x] = y`, when `y` is either a `dict` or a `Struct`); or
        * a `Array` (in the "set" context `a[x] = y`, when `y` is neither a
          `dict` nor a `Struct`).

    Alternatively, if the user wishes to specify which type the object should
    take, we implement the properties `as_cell`, `as_struct` and `as_num`.

    Therefore:
        * `a[x,y]             = num`    indicates that `a` is a numeric array;
        * `a[x,y]             = struct` indicates that `a` is a numeric array;
        * `a[x,y].f           = any`    indicates that `a` is a struct array;
        * `a(x,y).f           = any`    indicates that `a` is a cell array that contains a struct;
        * `a.f                = any`    indicates that `a` is a struct.

    And explictly:
        * `a.as_cell[x,y]     = any`    indicates that `a` is a cell array;
        * `a.as_struct[x,y].f = any`    indicates that `a` is a struct array;
        * `a.as_cell[x,y].f   = any`    indicates that `a` is a cell array that contains a struct;
        * `a.as_num[x,y]      = num`    indicates that `a` is a numeric array.
    """

    def __init__(self, parent=None):
        super().__init__()
        self._parent = parent
        self._array = None

    def _finalize(self):
        obj = self._array
        if obj is not None:
            return obj
        if self._parent is not None:
            return self._parent._DEFAULT()
        return asnum([])

    # def __str__(self):
    #     return self._finalize().__str__()

    # def __repr__(self):
    #     return self._finalize().__repr__()

    @property
    def as_cell(self):
        if self._array is None:
            self._array = Cell()
            if self._parent is not None:
                self._parent._finalize()
        return self._array

    @property
    def as_struct(self):
        if self._array is None:
            self._array = Struct()
            if self._parent is not None:
                self._parent._finalize()
        return self._array

    @property
    def as_num(self):
        if self._array is None:
            self._array = Array()
            if self._parent is not None:
                self._parent._finalize()
        return self._array

    def __call__(self, *index):
        return self.as_cell(*index)

    def __getitem__(self, index):
        return self.as_struct[index]

    def __getattr__(self, key):
        if key in ("_array", "_parent"):
            return super().__getattr__(key)
        return self.as_struct[key]

    def __setitem__(self, index, value):
        if self._array is not None:
            array = self._array
        elif isinstance(value, (dict, Struct)):
            array = self.as_struct
        elif isinstance(value, (tuple, Cell)):
            array = self.as_cell
            if isinstance(value, tuple):
                value = cell(*value)
        else:
            array = self.as_num
        array[index] = value

    def __setattr__(self, key, value):
        if key in ("_array", "_parent"):
            return super().__setattr__(key, value)
        self.as_struct[key] = value


class _WrappedArray(np.ndarray, _MatlabArray):
    """
    Base class for "arrays of things" (Array, Cell, Struct.)
    """

    # Value used for delayed arrays whose type cannot be guessed
    _DEFAULT = classmethod(lambda cls: asnum([]))

    def _EMPTY(self, n):
        raise NotImplementedError

    @classmethod
    def _parse_args(cls, *args, **kwargs):
        # split size / input / keyword arguments
        args, shape, obj = list(args), [], None
        while args and isinstance(args[0], int):
            shape.append(args.pop(0))
        if not shape:
            if args and not isinstance(args[0], (str, np.dtype, type)):
                obj = args.pop(0)
        if args:
            if "dtype" in kwargs:
                raise TypeError(
                    f"{cls.__name__}() got multiple values for "
                    f"argument 'dtype'"
                )
            kwargs["dtype"] = args.pop(0)
        if args:
            if "order" in kwargs:
                raise TypeError(
                    f"{cls.__name__}() got multiple values for "
                    f"argument 'order'"
                )
            kwargs["order"] = args.pop(0)
        if args:
            raise TypeError(
                f"{cls.__name__}() takes from 1 to 3 positional "
                "arguments but more were given"
            )
        if hasattr(obj, "__iter__") and not hasattr(obj, "__len__"):
            # save iterator values in a list
            obj = list(obj)
        return shape, obj, kwargs

    @property
    def as_num(self):
        raise TypeError(f"Cannot interpret a {type(self).__name__} as a numeric array")

    @property
    def as_cell(self):
        raise TypeError(f"Cannot interpret a {type(self).__name__} as a cell")

    @property
    def as_struct(self):
        raise TypeError(f"Cannot interpret a {type(self).__name__} as a struct")

    def append(self, value):
        """List-like API."""
        # NOTE/FIXME:
        #   we use an array, not a list, so appending through += is not allowed.
        self.resize([len(self)+1] + list(self.shape[1:]))
        self[-1] = value

    def extend(self, value):
        """List-like API."""
        # NOTE/FIXME:
        #   we use an array, not a list, so extending through += is not allowed.
        init_len = len(self)
        batch = len(self) + len(value)
        shape = np.broadcast_shape(self.shape, value.shape)
        self.resize([batch] + list(shape))
        self[init_len:] = value

    def __str__(self):
        return np.array_str(self)

    def __repr__(self):
        return np.array_str(self)

    def _iterindex(self):
        """Iterator across all multi-dimensional indices."""
        return itertools.product(*(range(x) for x in self.shape))

    def _iterall(self):
        """Iterator across all elements. Yields (index, element)."""
        if len(self.shape) == 0:
            yield (Ellipsis, self.reshape([-1])[0])
            return
        for index in self._iterindex():
            yield index, self[index]

    def __getitem__(self, index):
        """Resize array if needed, then fallback to np.ndarray indexing."""
        try:
            return super().__getitem__(index)
        except IndexError:
            self._resize_for_index(index)
            return super().__getitem__(index)

    def __setitem__(self, index, value):
        """Resize array if needed, then fallback to np.ndarray indexing."""
        value = asmatlab(value)
        try:
            return super().__setitem__(index, value)
        except IndexError:
            self._resize_for_index(index)
            return super().__setitem__(index, value)

    def _resize_for_index(self, index):
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
        shape, new_shape = list(self.shape), []
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
        view_index = tuple(slice(x, None) for x in self.shape)
        self.resize(new_shape, refcheck=False)
        view = self[view_index]
        new_data = self._EMPTY(view.size)
        if isinstance(new_data, np.ndarray):
            new_data = new_data.reshape(view.shape)
        self[view_index] = new_data

    def _finalize(self):
        """Transform all DelayedArrays into concrete arrays."""
        for i, elem in self._iterall():
            if isinstance(elem, _MatlabArray):
                self[i] = elem._finalize()
            else:
                self[i] = asmatlab(elem)
        return self


class Array(_WrappedArray):
    """
    Numeric array, compatible with matlab arrays.

    ```python
    # Instantiate from size
    Array(N, M, ...)
    Array([N, M, ...])

    # Instantiate from existing numeric array
    Array(other_array)

    # Other options
    Array(..., dtype=None, order=None, *, device=None, copy=None, like=None)
    ```
    """
    def _EMPTY(self, n):
        # Zero-fill when resizing
        return 0

    def __new__(cls, *args, **kwargs):
        # split size / input / keyword arguments
        shape, obj, kwargs = cls._parse_args(*args, **kwargs)

        if obj is None:
            # Array(M, N, ...)
            obj = super().__new__(cls, shape, **kwargs)
            if not issubclass(obj.dtype.type, np.number):
                raise TypeError("Array data type must be numeric")
            return obj

        if (
            hasattr(obj, "__len__") and
            (len(obj) == 0 or all(isinstance(x, int) for x in obj))
        ):
            # Array([M, N, ...]) -> Array(M, N, ...)
            return cls(*obj, **kwargs)

        # Array(array_like)
        obj = np.asanyarray(obj, **kwargs)
        if not issubclass(np.asarray(obj).dtype.type, np.number):
            raise TypeError("Array data type must be numeric")
        return np.ndarray.view(obj, Array)

    @property
    def as_num(self):
        return self

    def _finalize(self):
        # Nothing to do, numeric array cannot contain python objects.
        return self


class Cell(_WrappedArray):
    """
    Cell array, compatible with matlab cells.

    ```python
    # Instantiate from size
    Cell(N, M, ...)
    Cell([N, M, ...])

    # Instantiate from existing cell array
    Cell(other_cell)

    # Other options
    Cell(..., dtype=None, order=None, *, device=None, copy=None, like=None)

    # Instantiate from elements
    cell(x, y, z)
    ```
    """

    # TODO:
    #   I am thinking that cells should behave more like
    #   "multidimensional tuples/lists" than "ndarray".
    #   This means that:
    #       * we should hide all math functions.
    #       * `__add__`, `__iadd__`, `__radd__` should fallback to `extend()`,
    #         as in tuples, rather than `np.add` as in arrays.
    #       * "scalar" cells should be forbidden (already the case at
    #         construction, but we should also check that reshape/view do
    #         not return scalar cells).
    #       * maybe we should inherit from `tuple` (or `list`?).
    #         I think that most of the list methods make sense if
    #         we treat multidimensional cells as "lists of lists".
    #         The only treaky ones to implement are `insert/pop/remote`
    #         because they require "moving" data around.

    # Which value should we use as default in cell?
    #   * `None` is the most pythonic value
    #   * Matlab uses an empty numeric array (`asnum([])`)
    #   * Or we could use a scalar numeric array with value zero (`asnum(0.)`)
    # I am using `asnum([])` for now to be consistent with Matlab.
    _DEFAULT = classmethod(lambda cls: asnum([]))

    def _EMPTY(self, n):
        data = np.empty([n], dtype=object)
        for i in range(n):
            data[i] = _DelayedArray(self)
        return data

    def __new__(cls, *args, **kwargs):
        # split size / input / keyword arguments
        shape, obj, kwargs = cls._parse_args(*args, **kwargs)
        kwargs["dtype"] = object

        if obj is None:
            # Cell(M, N, ...)
            if len(shape) == 0:
                # Scalar cells are forbidden
                # (also, default cells must be 0-sized vectors)
                shape = [0]
            obj = super().__new__(cls, shape, **kwargs)
            if cls._DEFAULT() is not None:
                for i in obj._iterindex():
                    obj[i] = cls._DEFAULT()
            return obj

        if (
            hasattr(obj, "__len__") and
            (len(obj) == 0 or all(isinstance(x, int) for x in obj))
        ):
            # Cell([M, N, ...]) -> Array(M, N, ...)
            return cls(*obj, **kwargs)

        # Cell(cell_like)
        obj = np.asanyarray(obj, **kwargs)
        return np.ndarray.view(obj, Cell)

    @property
    def as_cell(self):
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


class Struct(_WrappedArray):
    """
    Struct array, compatible with matlab structs.

    ```python
    # Instantiate from size
    Struct(N, M, ...)
    Struct([N, M, ...])

    # Instantiate from existing struct array
    Struct(other_struct)

    # Instantiate from dictionary
    Struct({"a": x, "b": y})
    Struct(a=x, b=y)
    ```
    """
    # Same point as for cells (see comment)
    _DEFAULT = classmethod(lambda cls: asnum([]))

    # List of public attributes and methods from the ndarray class that we
    # keep in Struct.
    # Most of these have "external" version (e.g. `np.ndim(x)`), so could
    # also be hidden if we suggest people use external functions.
    _NDARRAY_ATTRS = (
        "dtype",    # !! does not have `np.dtype`
        "ndim",     # has `np.ndim`
        "shape",    # has `np.shape`
        "size",     # has `np.size`
        "strides",  # !! does not have `np.strides`
        "reshape",  # has `np.reshape`
        "resize",   # !! does not have `np.resize`, can use `np.ndarray.resize`
        "squeeze",  # has `np.squeeze`
        "copy",     # has `np.copy`
        "tolist",   # !! does not have `np.tolist`, can use `np.ndarray.tolist`
        "flatten",  # !! does not have `np.flatten`, can use `np.ndarray.flatten`
        "ravel",    # has `np.ravel`
        "flat",     # !! does not have `np.flat`, can use `np.ndarray.flat` or `np.flatiter`
        "T",        # !! does not have `np.T`
        # MAYBE:
        # view, item, itemset, swapaxes, transpose, data, dtype,
    )

    def _EMPTY(self, n):
        data = np.empty([n], dtype=dict)
        for i in range(n):
            data[i] = {}
        return data

    @classmethod
    def _parse_args(cls, *args, **kwargs):
        # split size / input / keyword arguments
        args, shape, obj = list(args), [], None
        while args and isinstance(args[0], int):
            shape.append(args.pop(0))
        if args and not shape:
            obj = args.pop(0)
        if args:
            raise TypeError(
                "Struct() takes 1 positional arguments but more were given"
            )
        if hasattr(obj, "__iter__") and not hasattr(obj, "__len__"):
            # save iterator values in a list
            obj = list(obj)
        return shape, obj, kwargs

    def __new__(cls, *args, **kwargs):
        shape, obj, kwargs = cls._parse_args(*args, **kwargs)

        if obj is None:
            # Struct(M, N, ...)
            obj = super().__new__(cls, shape, dtype=dict)
            for index, _ in obj._iterall():
                np.ndarray.__setitem__(obj, index, dict(**kwargs))
            return obj

        if (
            hasattr(obj, "__len__") and not isinstance(obj, (dict, Struct))
            and (len(obj) == 0 or all(isinstance(x, int) for x in obj))
        ):
            # Struct([M, N, ...]) -> Struct(M, N, ...)
            return cls(*obj, **kwargs)

        # Struct([array_like of] dict or struct)
        obj = np.asanyarray(obj, dtype=dict)
        obj = np.ndarray.view(obj, Struct)
        arr = np.ndarray.view(obj, np.ndarray)

        rebuild = False
        for i in itertools.product(*(range(x) for x in arr.shape)):
            if isinstance(arr[i], np.ndarray):
                tmp = np.ndarray.view(arr[i], dict, np.ndarray)
                if len(arr[i].shape) == 0:
                    tmp = tmp.item()
                else:
                    tmp = tmp.tolist()
                arr[i] = tmp
                rebuild = True
        if rebuild:
            return cls(arr, **kwargs)

        for i in itertools.product(*(range(x) for x in arr.shape)):
            if not isinstance(arr[i], dict):
                raise TypeError("Cannot convert", obj, "to Struct.")

        if kwargs:
            obj.update(kwargs)
        return obj

    @property
    def as_struct(self):
        return self

    def _elem(self):
        # In a Struct, single-element indexing returns a scalar array of
        # dict (i.e., it's shape is an empty list []). This allows us to never
        # expose the dictionary itself. However, we do sometimes need to access
        # the dictionary, in which case we use this helper.
        if len(self.shape) == 0:
            flat = self.reshape([-1])
            elem = np.ndarray.__getitem__(flat, 0)
            return elem
        raise ValueError("Should only be called on 'scalar struct arrays'.")

    def _iterall(self):
        # Make iterator return the underlying `dict`, not the struct wrapper.
        for index, elem in super()._iterall():
            yield index, elem._elem()

    def _asdict(self):
        # scalar struct -> return the underlying dictionary
        # otherwise     -> reverse array/dict order -> dict of cells of values
        if len(self.shape) == 0:
            return self._elem()
        return {
            key: cell(*[
                elem.get(key, self._DEFAULT()) for _, elem in self._iterall()
            ]).reshape(self.shape)
            for key in self._allkeys()
        }

    def _allkeys(self):
        elems = {}
        for _, elem in self._iterall():
            elems.update(elem)
        return elems.keys()

    def keys(self):
        return self._asdict().keys()

    def items(self):
        return self._asdict().items()

    def values(self):
        return self._asdict().values()

    def setdefault(self, key, value):
        for _, elem in self._iterall():
            elem.setdefault(key, asmatlab(value))

    def update(self, other):
        if isinstance(other, Struct):
            other = np.broadcast_to(self)
            for i, elem in self._iterall():
                elem.update(asmatlab(other[i]))
        else:
            for _, elem in self._iterall():
                elem.update(asmatlab(other))

    def __getitem__(self, index):
        if isinstance(index, str):
            return getattr(self, index)
        else:
            obj = super().__getitem__(index)
            if not isinstance(obj, Struct):
                if not isinstance(index, tuple):
                    index = (index,)
                index += (None,)
                obj = super().__getitem__(index)
                obj = obj.reshape([])
            return obj

    def __setitem__(self, index, value):
        value = asmatlab(value)
        if isinstance(index, str):
            setattr(self, index, value)
        else:
            super().__setitem__(index, value)

    def __getattribute__(self, key):
        asnumpy = np.asarray(self)
        if (
            hasattr(asnumpy, key) and
            key[:1] != "_" and
            key not in type(self)._NDARRAY_ATTRS
        ):
            raise AttributeError("")
        return super().__getattribute__(key)

    def __getattr__(self, key):
        if key.startswith("_"):
            # FIXME: do we need this exception?
            raise KeyError(key)
        allkeys = self._allkeys()
        for _, elem in self._iterall():
            # NOTE
            #   We only insert a DelayedArray if it is a completely new key.
            #   Otherwise the default value is [], as per matlab.
            elem.setdefault(
                key,
                self._DEFAULT() if key in allkeys else
                _DelayedArray(self)
            )
        return self._asdict()[key]

    def __setattr__(self, key, value):
        if len(self.shape) == 0:
            # Scalar array: assign value to the field
            if isinstance(value, unpack):
                if len(value.shape) > 0:
                    raise ValueError("Cannot broadcast.")
                value = np.asarray(value)

            self._elem()[key] = asmatlab(value)

        elif isinstance(value, unpack):
            # Each element in the struct array is matched with an element in
            # the "unpack" array.
            value = np.broadcast_to(value, self.shape)
            for i, elem in self._iterall():
                elem[key] = asmatlab(value[i])

        else:
            # Assign the same value to all elements in the struct array.
            for _, elem in self._iterall():
                elem[key] = asmatlab(value)

    def __delattr__(self, key):
        if key not in self._allkeys():
            raise AttributeError(key)
        for _, elem in self._iterall():
            if key in elem:
                elem.__delitem__(key)

    def __delitem__(self, key):
        if isinstance(key, str):
            try:
                return self.__delattr__(key)
            except AttributeError as e:
                raise KeyError(e)
        return super().__delitem__(key)

    def _finalize(self):
        for i, elem in self._iterall():
            if not isinstance(elem, dict):
                np.ndarray.__setitem__(self, i, {})
                continue
            for key, value in elem.items():
                if isinstance(value, _MatlabArray):
                    elem[key] = value._finalize()
                else:
                    elem[key] = asmatlab(elem[key])
        return self

    def _as_matlab_object(self):
        array = np.reshape(np.asarray(self), [-1], order="F")
        return dict(
            type__='structarray',
            size__=np.array([[*self.shape]]),
            data__=_as_matlab_object(array)
        )

    @staticmethod
    def _from_matlab_object(objdict):
        if objdict['type__'] != 'structarray':
            raise TypeError('objdict is not a structarray')
        size = np.array(objdict['size__'], dtype=np.uint32).ravel()
        data = np.array(objdict['data__'], dtype=object)
        data = data.reshape(size)
        try:
            obj = data.view(Struct)
        except Exception:
            raise RuntimeError(
                f'Failed to construct Struct data:\n'
                f'  data={data}\n'
                f'  objdict={objdict}'
            )
        return asmatlab(obj)


class MatlabClassWrapper:
    _subclasses = dict()

    def _as_matlab_object(self):
        return self._objdict

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
            cls.__call__    = MatlabClassWrapper.__call

        if hasattr(cls, 'subsasgn'):
            cls.__setitem__ = MatlabClassWrapper.__setitem

        MatlabClassWrapper._subclasses[cls.__name__] = cls

    @staticmethod
    def _from_matlab_object(objdict):
        if objdict['class__'] in MatlabClassWrapper._subclasses.keys():
            obj = MatlabClassWrapper._subclasses[objdict['class__']](_objdict=objdict)
        else:
            warnings.warn(f'Unknown Matlab class type: {objdict["class__"]}')
            obj = MatlabClassWrapper(_objdict=objdict)
        return obj

    def __getattr(self, key):
        try:
            return self.subsref({'type': '.', 'subs': key})
        except:
            raise AttributeError(key)

    def __getitem(self, ind):
        index = self._process_index(ind)

        try:
            return self.subsref({'type': '()', 'subs': index})
        except:
            try:
                return self.subsref({'type': '{}', 'subs': index})
            except:
                raise IndexError(index)

    def __setitem(self, ind, value):
        index = self._process_index(ind)

        try:
            return self.subsasgn({'type': '()', 'subs': index}, value)
        except:
            try:
                return self.subsasgn({'type': '{}', 'subs': index}, value)
            except:
                raise IndexError(index)

    def __call(self, *index):
        index = self._process_index(index)
        try:
            return self.subsref({'type': '{}', 'subs': index})
        except:
            raise IndexError(index)

    def _process_index(self, ind, k=1, n=1):
        try:
            return tuple(self._process_index(i, k+1, len(ind))
                    for k, i in enumerate(ind))
        except TypeError:
            pass

        if not hasattr(self, '__endfn'):
            self.__endfn = Runtime.call('str2func', 'end')

        end = lambda: Runtime.call(self.__endfn, self._as_matlab_object(), k, n)

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


class OldStruct(dict):
    """emulates struct with a dot.notation access to dictionary attributes"""
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __getattr__(self, item):
        if item.startswith('__'):
            raise AttributeError
        else:
            return dict.__getitem__(self, item)


class OldCell(list):
    """emulates matlab's cell"""
    def __init__(self, m, n):
        super().__init__([[] for j in range(n)] for i in range(m))

    def __getitem__(self, index):
        if isinstance(index, tuple):
            i, j = index
            return self[i][j]
        else:
            return super().__getitem__(index)

    def __setitem__(self, index, value):
        if isinstance(index, tuple):
            i, j = index
            xi = self[i]
            xi[j] = value
            self[i] = xi
        else:
            super().__setitem__(index, value)


class OldStructArray:
    def __init__(self, *structs):
        if len(structs) == 1:
            if isinstance(structs[0], OldStruct):
                structs = [structs[0]]
            else:
                if all(map(isinstance, structs[0],itertools.repeat(int))):
                    size = structs[0]
                    structs = np.fromiter(
                        map(
                            lambda i: dict(), range(int(np.prod(size)))),
                        dtype=object).reshape(size)
                elif all(map(isinstance, structs[0], itertools.repeat(dict))):
                    structs = structs[0]
                elif isinstance(structs[0], np.ndarray) \
                        and all(map(isinstance, structs[0].flat, itertools.repeat(dict))):
                    structs = structs[0]
                else:
                    raise TypeError(f'arguments not understood: {structs}')

        if isinstance(structs, np.ndarray):
            structs = np.fromiter(
                map(dict, structs.flat),
                dtype=object).reshape(structs.shape)
        else:
            structs = np.fromiter(
                map(dict, structs),
                dtype=object)

        if len(structs.shape) == 1:
            structs = structs[None, :]

        self._structs = structs
        self._objdict = dict(
            type__='structarray',
            size__=np.array([[*structs.shape]]),
            data__=[]
        )

    def __getitem__(self, index):
        try:
            len(index)
        except TypeError:
            index = (0, index)

        item = self._structs[index]
        if isinstance(item, dict):
            item = OldStruct(item)
        return item

    def keys(self):
        return set(
            itertools.chain.from_iterable(
                map(dict.keys, self._structs.flat)))

    def _as_matlab_object(self):
        _ = [*map(
            lambda arg: arg[0].__setitem__(arg[1], np.array([])),
            filter(
                lambda arg: arg[1] not in arg[0].keys(),
                itertools.product(self._structs.flat, self.keys())
            )
        )]
        objdict = self._objdict
        objdict['data__'] = np.reshape(self._structs, (-1,), order='F').tolist()
        return objdict

    def __repr__(self):
        return self._structs \
            .__repr__() \
            .replace('array([], dtype=float64)', 'empty') \
            .replace('matlab.double([])', 'empty') \
            .replace('array(', 'Struct(\n  data=') \
            .replace(', dtype=object', f',\n  keys={self.keys()}')

    @staticmethod
    def _from_matlab_object(objdict):
        if objdict['type__'] != 'structarray':
            raise TypeError('objdict is not a structarray')
        size = np.array(objdict['size__'], dtype=np.uint32).ravel()
        data = np.array(objdict['data__'], dtype=object)
        data = data.reshape(size)
        try:
            obj = OldStructArray(data)
        except Exception as e:
            raise RuntimeError(f'Failed to construct Struct data:\n  data={data}\n  objdict={objdict}')

        return obj
