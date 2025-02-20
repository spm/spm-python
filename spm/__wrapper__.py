try:
    from spm._spm import initialize
except ImportError as e:
    import os
    from textwrap import dedent
    installer_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '_spm',
        'resources',
        'RuntimeInstaller.install'
    )
    print(dedent(
        """
        Failed to import spm._spm. This can be due to a failure to find Matlab Runtime.
        Please verify that Matlab Runtime is installed and its path is set.
        See https://www.mathworks.com/help/compiler/mcr-path-settings-for-run-time-deployment.html
        for instructions on how to setup the path.
        If the issue persists, please open an issue with the entire error
        message at https://github.com/spm/spm-python/issues.
        """
    ))

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

    @staticmethod
    def _process_argin(*args, **kwargs):
        to_runtime = _MatlabTypeHelpers._to_runtime
        args = tuple(map(to_runtime, args))
        kwargs = dict(zip(kwargs.keys(), map(to_runtime, kwargs.values())))
        return args, kwargs

    @staticmethod
    def _process_argout(res):
        from_runtime = _MatlabTypeHelpers._from_any
        return from_runtime(res)


# ----------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------


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


class _MatlabTypeHelpers(object):
    """Helpers used by other classes."""

    @staticmethod
    def _to_cell(other) -> "Cell":
        """
        Convert (nested) list-like objects to cells.
        """
        other = np.asanyarray(other, dtype=object)
        return _MatlabType._from_any(np.ndarray.view(other, Cell))

    @staticmethod
    def _to_num(other) -> "Array":
        """
        Convert array-like objects to numeric arrays.
        """
        other = np.asanyarray(other)
        if not issubclass(other.dtype.type, np.number):
            other = np.asanyarray(other, dtype=np.float64)
        return np.ndarray.view(other, Array)

    @staticmethod
    def _to_struct(other) -> "Struct":
        """
        Convert (nested) dict-like objects to struct.
        Convert (array of) dict-like objects to struct array.
        """
        if isinstance(other, np.ndarray) and other.dtype in (object, dict):
            return _MatlabType._from_any(np.ndarray.view(other, Struct))
        return _MatlabType._from_any(Struct(other))

    @classmethod
    def _from_any(cls, other):
        """
        Convert python objects to `_MatlabType` objects
        (`Cell`, `Struct`, `Array`, `MatlabClassWrapper`).

        !!! warning "Conversion is performed in-place when possible."
        """
        #   - we do not convert to matlab's own array types
        #     (`matlab.double`, etc);
        #   - we do not convert to types that can be passed directly to
        #     the matlab bindings;
        #   - instead, we convert to python types that mimic matlab types.
        if isinstance(other, Array):
            return other

        if isinstance(other, Cell):
            for i, x in other._iterall():
                np.ndarray.__setitem__(other, i, cls._from_any(x))
            return other

        if isinstance(other, Struct):
            for i, x in other._iterall():
                for k, v in x.items():
                    x[k] = cls._from_any(v)
            return other

        if isinstance(other, dict):
            if "type__" in other:
                type__ = other["type__"]

                if type__ == "structarray":
                    # Matlab returns a list of dictionaries in data__
                    # and the array shape in size__.
                    return Struct._from_matlab_object(other)

                elif type__ == 'object':
                    # Matlab returns the object's fields serialized
                    # in a dictionary.
                    return MatlabClassWrapper._from_matlab_object(other)

                elif type__ == 'sparse':
                    # Matlab returns a dense version of the array in data__.
                    return np.asarray(
                        other['data__'], dtype=np.double
                    ).view(Array)

                else:
                    raise ValueError("Don't know what to do with type", type__)

            else:
                return cls._to_struct(other)

        if isinstance(other, (tuple, set)):
            return cls._to_cell(other)

        if isinstance(other, (list, np.ndarray, int, float, complex, bool)):
            try:
                return cls._to_num(other)
            except (ValueError, TypeError):
                return cls._to_cell(other)

        if isinstance(other, _MatlabType):
            if hasattr(other, "_finalize"):
                return other._finalize()
            else:
                return other

        if isinstance(other, str):
            return other

        if other is None:
            # This can happen when matlab code is called without `nargout`
            return other

        raise TypeError(
            f"Cannot convert {type(other).__name__} into a matlab object."
        )

    @classmethod
    def _to_runtime(cls, obj):
        """
        Convert object to representation that the matlab runtime understand.
        """
        _to_bindings = cls._to_runtime

        if hasattr(obj, "_as_matlab_object"):
            # class / structarray
            return obj._as_matlab_object()

        elif isinstance(obj, (list, tuple, set)):
            return type(obj)(map(_to_bindings, obj))

        elif isinstance(obj, dict):
            return type(obj)(zip(obj.keys(), map(_to_bindings, obj.values())))

        elif isinstance(obj, np.ndarray):
            obj = np.asarray(obj)
            if obj.dtype in (object, dict):
                shape, dtype = obj.shape, obj.dtype
                obj = np.fromiter(map(_to_bindings, obj.flat), dtype=dtype)
                obj = obj.reshape(shape)
                return obj.tolist()
            return obj

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


class _MatlabType(object):
    """Generic type for all objects that have an exact matlab equivalent."""


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
        * `a[x,y]             = num`    : `a` is a numeric array;
        * `a[x,y]             = struct` : `a` is a numeric array;
        * `a[x,y].f           = any`    : `a` is a struct array;
        * `a(x,y).f           = any`    : `a` is a cell array that contains a struct;
        * `a.f                = any`    : `a` is a struct.

    And explictly:
        * `a.as_cell[x,y]     = any`    : `a` is a cell array;
        * `a.as_struct[x,y].f = any`    : `a` is a struct array;
        * `a.as_cell[x,y].f   = any`    : `a` is a cell array that contains a struct;
        * `a.as_num[x,y]      = num`    : `a` is a numeric array.
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
        return _MatlabTypeHelpers._to_num([])

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
                value = Cell.from_iterable(value)
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
    _DEFAULT = classmethod(lambda cls: _MatlabTypeHelpers._to_num([]))

    def _EMPTY(self, n):
        raise NotImplementedError

    @classmethod
    def _parse_args(cls, *args, __has_dtype=True, __has_order=True, **kwargs):
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
        shape : list[int]
        obj : array-like | None
        kwargs : dict
        """
        # split size / input / keyword arguments

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
            not shape and hasattr(obj, "__len__") and
            (len(obj) == 0 or all(isinstance(x, int) for x in obj))
        ):
            shape, obj = obj, None

        return shape, obj, kwargs

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

    def __str__(self):
        return np.array_str(self)

    def __repr__(self):
        return np.array_str(self)

    def _iterindex(self):
        """Iterator across all multi-dimensional indices."""
        return itertools.product(*(range(x) for x in self.shape))

    def _iterall(self):
        """
        Iterator across all elements. Yields (index, element).
        If object has an empty shape, return (Ellipsis, item()).
        """
        if len(self.shape) == 0:
            yield (Ellipsis, np.ndarray.item(self))
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
        value = _MatlabTypeHelpers._from_any(value)
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
        np.ndarray.resize(self, new_shape, refcheck=False)
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
                self[i] = _MatlabTypeHelpers._from_any(elem)
        return self


class _ListishMixin:
    """These methods are implemented in Cell and Array, but not Struct."""

    def append(self, value):
        """List-like API."""
        new_shape = list(np.shape(self))
        new_shape[0] += 1
        np.ndarray.resize(new_shape, refcheck=False)
        self[-1] = value

    def extend(self, value):
        """List-like API."""
        init_len = len(self)
        batch = len(self) + len(value)
        shape = np.broadcast_shape(np.shape(self)[1:], np.shape(value)[1:])
        new_shape = [batch] + list(shape)
        np.ndarray.resize(self, new_shape, refcheck=False)
        self[init_len:] = value

    def clear(self):
        """Remove all items by setting the first axis to have size 0."""
        zero_shape = list(np.shape(self))
        zero_shape[0] = 0
        np.ndarray.resize(zero_shape, refcheck=False)


class _ListLikeMixin:
    """These methods are implemented in Cell, but not in Array or Struct."""

    def __add__(self, other):
        other = _MatlabTypeHelpers._to_cell(other)
        return np.concatenate([self, other])

    def __radd__(self, other):
        other = _MatlabTypeHelpers._to_cell(other)
        return np.concatenate([other, self])

    def __iadd__(self, other):
        return self.append(other)

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

    def count(self, value):
        """Return number of occurrences of value."""
        # FIXME:
        #   This is tricky. Should a cell array behave like:
        #   1. a list of list?
        #   2. as if it was flattened?
        #   3. do we use strict equality (same shape) or broacasted equality?
        return sum([np.all(elem == value) for elem in self])

    def index(self, value):
        """Return first index of value."""
        # FIXME:
        #   This is also tricky for the same reasons.
        for i, elem in enumerate(self):
            if np.all(elem == value):
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
            np.ndarray.sort(self, kind="stable", axis=axis)
            if reverse:
                self.reverse()

    def __delitem__(self, index):
        if index < 0:
            index = len(self) + index
        new_shape = list(np.shape(self))
        new_shape[0] -= 1
        self[index:-1] = self[index+1:]
        np.ndarray.resize(self, new_shape, refcheck=False)


class Array(_WrappedArray, _ListishMixin):
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


class Cell(_WrappedArray, _ListLikeMixin):
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
    _DEFAULT = classmethod(lambda _: _MatlabTypeHelpers._to_num([]))

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

        # Cell(cell_like)
        obj = np.asanyarray(obj, **kwargs)
        return np.ndarray.view(obj, Cell)

    @classmethod
    def from_iterable(cls, iterable):
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
    _DEFAULT = classmethod(lambda cls: _MatlabTypeHelpers._to_num([]))

    def _EMPTY(self, n):
        data = np.empty([n], dtype=dict)
        for i in range(n):
            data[i] = {}
        return data

    def __new__(cls, *args, **kwargs):
        kwargs["__has_dtype"] = False
        kwargs["__has_order"] = False
        shape, obj, kwargs = cls._parse_args(*args, **kwargs)

        if obj is None:
            # Struct(M, N, ...)
            obj = super().__new__(cls, shape, dtype=dict)
            for index, _ in obj._iterall():
                # NOTE: we use _iterall (not _iterindex) to cover
                # the case of scalar (empty-shaped) struct.
                np.ndarray.__setitem__(obj, index, dict(**kwargs))
            return obj

        # Struct([array_like of] dict or struct)
        obj = np.asanyarray(obj, dtype=dict)
        obj = np.ndarray.view(obj, Struct)
        arr = np.ndarray.view(obj, np.ndarray)

        rebuild = False
        for i, _ in obj._iterall():
            # NOTE: we use _iterall (not _iterindex) to cover
            # the case of scalar (empty-shaped) struct.
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

        for i, _ in obj._iterall():
            if not isinstance(arr[i], dict):
                raise TypeError("Cannot convert", obj, "to Struct.")

        if kwargs:
            obj.update(kwargs)
        return obj

    @property
    def as_struct(self):
        return self

    def _asdict(self):
        # scalar struct -> return the underlying dictionary
        # otherwise     -> reverse array/dict order -> dict of cells of values
        if len(self.shape) == 0:
            return np.ndarray.item(self)
        return {
            key: Cell.from_iterable([
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
            elem.setdefault(key, _MatlabTypeHelpers._from_any(value))

    def update(self, other):
        if isinstance(other, Struct):
            other = np.broadcast_to(self)
            for i, elem in self._iterall():
                elem.update(_MatlabTypeHelpers._from_any(other[i]))
        else:
            for _, elem in self._iterall():
                elem.update(_MatlabTypeHelpers._from_any(other))

    def __getitem__(self, index):
        if isinstance(index, str):
            return getattr(self, index)
        else:
            obj = super().__getitem__(index)
            if not isinstance(obj, Struct):
                # We've indexed a single element, but we do not want
                # to expose the underlying dictionary. Instead,
                # we return an empty-sized view of the element, which
                # is still of type `Struct`.
                if not isinstance(index, tuple):
                    index = (index,)
                index += (None,)
                obj = super().__getitem__(index)
                obj = np.reshape(obj, [])
            return obj

    def __setitem__(self, index, value):
        value = _MatlabTypeHelpers._from_any(value)
        if isinstance(index, str):
            setattr(self, index, value)
        else:
            super().__setitem__(index, value)

    def __getattribute__(self, key):
        asnumpy = np.asarray(self)
        if hasattr(asnumpy, key) and key[:1] != "_":
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

            np.ndarray.item(self)[key] = _MatlabTypeHelpers._from_any(value)

        elif isinstance(value, unpack):
            # Each element in the struct array is matched with an element in
            # the "unpack" array.
            value = np.broadcast_to(value, self.shape)
            for i, elem in self._iterall():
                elem[key] = _MatlabTypeHelpers._from_any(value[i])

        else:
            # Assign the same value to all elements in the struct array.
            for _, elem in self._iterall():
                elem[key] = _MatlabTypeHelpers._from_any(value)

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
                    elem[key] = _MatlabTypeHelpers._from_any(elem[key])
        return self

    def _as_matlab_object(self):
        array = np.reshape(np.asarray(self), [-1], order="F")
        return dict(
            type__='structarray',
            size__=np.array([[*self.shape]]),
            data__=_MatlabTypeHelpers._to_runtime(array)
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
        return _MatlabTypeHelpers._from_any(obj)


class MatlabClassWrapper(_MatlabClass):
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
            cls.__call__ = MatlabClassWrapper.__call

        if hasattr(cls, 'subsasgn'):
            cls.__setitem__ = MatlabClassWrapper.__setitem

        MatlabClassWrapper._subclasses[cls.__name__] = cls

    @staticmethod
    def _from_matlab_object(objdict):
        if objdict['class__'] in MatlabClassWrapper._subclasses.keys():
            obj = MatlabClassWrapper._subclasses[objdict['class__']](
                _objdict=objdict
            )
        else:
            warnings.warn(f'Unknown Matlab class type: {objdict["class__"]}')
            obj = MatlabClassWrapper(_objdict=objdict)
        return obj

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
            return Runtime.call(self.__endfn, self._as_matlab_object(), k, n)

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
