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
from collections.abc import (
    MutableSequence, MutableMapping, KeysView, ValuesView, ItemsView
)

# if scipy is available, convert matlab sparse matrices scipy.sparse
# otherwise, convert them to dense numpy arrays
try:
    from scipy import sparse
except (ImportError, ModuleNotFoundError):
    sparse = None

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
        to_runtime = MatlabType._to_runtime
        args = tuple(map(to_runtime, args))
        kwargs = dict(zip(kwargs.keys(), map(to_runtime, kwargs.values())))
        return args, kwargs

    @staticmethod
    def _process_argout(res):
        return MatlabType.from_any(res)


# ----------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------


class unpack:
    """
    Helper class to assign values into a specific field of a Struct array.

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
    # The idea is to have a type that tells Struct.__setattr__
    # that we want to broadcast the object before assigning it to the field.
    # We let the target struct tell this object which field is being assigned
    # and this object transforms itself into a struct array with a single
    # field (but multiple) elements. We can then let broadcasting
    # do its magic.

    def __init__(self, *args):
        self.args = np.empty([len(args)], dtype=object)
        self.args[...] = args

    def to_struct(self, name: str) -> "Struct":
        """
        Convert into a struct array with a single field.
        """
        s = Struct(len(self.args))
        for i in range(len(s)):
            s[i][name] = self.args[i]
        return s


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
        #   - we do not convert to matlab's own array types
        #     (`matlab.double`, etc);
        #   - we do not convert to types that can be passed directly to
        #     the matlab bindings;
        #   - instead, we convert to python types that mimic matlab types.
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
                    data = np.asarray(other['data__'], dtype=np.double)
                    if sparse:
                        # TODO: Implement a SparseArray wrapper?
                        return sparse.coo_array(data)
                    else:
                        return data.view(Array)

                else:
                    raise ValueError("Don't know what to do with type", type__)

            else:
                return Struct.from_any(other)

        if isinstance(other, (tuple, set)):
            # nested tuples are cells of cells, not cell arrays
            return Cell.from_iterable(other)

        if isinstance(other, (list, np.ndarray, int, float, complex, bool)):
            try:
                return Array.from_any(other)
            except (ValueError, TypeError):
                return Cell.from_iterable(other)

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
        _to_runtime = cls._to_runtime

        if isinstance(obj, MatlabType):
            # class / structarray / cell
            return obj._as_runtime()

        elif isinstance(obj, (list, tuple, set)):
            return type(obj)(map(_to_runtime, obj))

        elif isinstance(obj, dict):
            return type(obj)(zip(obj.keys(), map(_to_runtime, obj.values())))

        elif isinstance(obj, np.ndarray):
            obj = np.asarray(obj)
            if obj.dtype in (object, dict):
                shape, dtype = obj.shape, obj.dtype
                obj = np.fromiter(map(_to_runtime, obj.flat), dtype=dtype)
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


class AnyMatlabArray(MatlabType):
    """Base class for all matlab-like arrays (numeric, cell, struct)."""


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
        obj = self._array
        if obj is not None:
            return obj
        if self._parent is not None:
            return self._parent._DEFAULT()
        return Array.from_any([])

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
            # FIXME: this case should have been caught by __getattribute__
            # -> check if it is, or why it isn't.
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


class _WrappedArray(np.ndarray, AnyMatlabArray):
    """
    Base class for "arrays of things" (Array, Cell, Struct.)
    """

    # Value used for delayed arrays whose type cannot be guessed
    # Can be overloaded in Array/Cell/Struct.
    _DEFAULT = classmethod(lambda cls: Array.from_any([]))

    # Value used to fill-in a newly allocated array.
    # Must be implemented in Array/Cell/Struct.
    def _EMPTY(self, n):
        raise NotImplementedError

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
        shape : list[int]
        obj : array-like | None
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
        return itertools.product(*(range(x) for x in np.shape(self)))

    def _iterall(self):
        """
        Iterator across all elements. Yields (index, element).
        If object has an empty shape, return (Ellipsis, item()).
        """
        asarray = np.ndarray.view(self, np.ndarray)
        if np.ndim(self) == 0:
            # yield (Ellipsis, np.ndarray.item(self))
            yield (Ellipsis, asarray.item())
            return
        for index in self._iterindex():
            yield index, asarray[index]

    def __getitem__(self, index):
        """Resize array if needed, then fallback to np.ndarray indexing."""
        try:
            return super().__getitem__(index)
        except IndexError:
            self._resize_for_index(index)
            return super().__getitem__(index)

    def __setitem__(self, index, value):
        """Resize array if needed, then fallback to np.ndarray indexing."""
        value = MatlabType.from_any(value)
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
        view_index = tuple(slice(x, None) for x in np.shape(self))
        np.ndarray.resize(self, new_shape, refcheck=False)
        view = self[view_index]
        new_data = self._EMPTY(view.size)
        if isinstance(new_data, np.ndarray):
            new_data = new_data.reshape(view.shape)
        self[view_index] = new_data

    def _finalize(self):
        """Transform all DelayedArrays into concrete arrays."""
        for i, elem in self._iterall():
            if isinstance(elem, AnyMatlabArray):
                self[i] = elem._finalize()
            else:
                self[i] = MatlabType.from_any(elem)
        return self


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
    #   * __delitem__

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


class _ListMixin(_ListishMixin, MutableSequence):
    """These methods are implemented in Cell, but not in Array or Struct."""

    # NOTE:
    #   The only abstract methods from MutableSequence are:
    #   * __getitem__   -> inherited from np.ndarray
    #   * __setitem__   -> inherited from np.ndarray
    #   * __delitem__   -> implemented here
    #   * __len__       -> inherited from np.ndarray
    #   * insert        -> implemented here
    #
    #   MutableSequence implements the following non-abstract methods,
    #   but we overload them for speed:
    #   * __iter__      -> inherited from np.ndarray
    #   * __reversed__  -> implemented here
    #   * index         -> implemented here
    #   * count         -> implemented here
    #   * append        -> inherited from _ListishMixin
    #   * clear         -> inherited from _ListishMixin
    #   * reverse       -> implemented here
    #   * extend        -> inherited from _ListishMixin
    #   * pop           -> implemented here
    #   * remove        -> implemented here
    #   * __iadd__      -> implemented here
    #
    #   Mutable implements the following non-abstract methods, which
    #   we keep
    #   * __contains__  -> FIXME: should we implement it?

    # --- magic --------------------------------------------------------

    def __add__(self, other):
        other = Cell.from_any(other)
        return np.concatenate([self, other])

    def __radd__(self, other):
        other = Cell.from_any(other)
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

    def __reversed__(self):
        # FIXME: this returns a view -- should we make a copy?
        return self[::-1]

    def __delitem__(self, index):
        if index < 0:
            index = len(self) + index
        new_shape = list(np.shape(self))
        new_shape[0] -= 1
        self[index:-1] = self[index+1:]
        np.ndarray.resize(self, new_shape, refcheck=False)

    # need to explicitely reference np.ndarray methods otherwise it
    # goes back to MutableSequence, which raises.
    __getitem__ = np.ndarray.__getitem__
    __setitem__ = np.ndarray.__setitem__

    # --- sequence -----------------------------------------------------

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
            np.ndarray.sort(self, kind=kind, axis=axis)
            if reverse:
                self.reverse()


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
    # Value used to fill-in a newly allocated array -> zero
    def _EMPTY(self, n) -> int:
        return 0

    def __new__(cls, *args, **kwargs):
        shape, obj, kwargs = cls._parse_args(*args, **kwargs)

        if obj is None:
            # Array(M, N, ...)
            obj = super().__new__(cls, shape, **kwargs)
            if not issubclass(obj.dtype.type, np.number):
                raise TypeError("Array data type must be numeric")
            return obj

        # Array(array_like)
        obj = np.asanyarray(obj, **kwargs)
        dtype = np.ndarray.view(obj, np.ndarray).dtype
        if not issubclass(dtype.type, np.number):
            raise TypeError("Array data type must be numeric")
        return np.ndarray.view(obj, Array)

    @classmethod
    def from_any(cls, other) -> "Array":
        """
        Convert array-like objects to numeric arrays.
        """
        other = np.asanyarray(other)
        if not issubclass(other.dtype.type, np.number):
            other = np.asanyarray(other, dtype=np.float64)
        return np.ndarray.view(other, Array)

    def _as_runtime(self):
        return np.ndarray.view(self, np.ndarray)

    @classmethod
    def _from_runtime(cls, other):
        return cls.from_any(other)

    @property
    def as_num(self):
        return self

    def _finalize(self):
        # Nothing to do, numeric array cannot contain python objects.
        return self


class Cell(_ListMixin, _WrappedArray):
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
    Cell.from_iterable([x, y, z])
    ```
    """

    # NOTE
    #   _ListMixin must have precedence over _WrappedArray so that its
    #   method overload those from np.ndarray. This is why the
    #   inheritence order is (_ListMixin, _WrappedArray).

    # FIXME: Which value should we use as default in cell?
    #   * `None` is the most pythonic value
    #   * Matlab uses an empty numeric array (`asnum([])`)
    #   * Or we could use a scalar numeric array with value zero (`asnum(0.)`)
    # I am using `asnum([])` for now to be consistent with Matlab.
    _DEFAULT = classmethod(lambda _: Array.from_any([]))

    # Value used to fill-in a newly allocated array -> delayed array
    def _EMPTY(self, n) -> np.ndarray:
        data = np.empty([n], dtype=object)
        for i in range(n):
            data[i] = DelayedArray(self)
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
    def from_any(cls, other) -> "Cell":
        """
        Convert (nested) list-like objects to cells.
        """
        if isinstance(other, dict) and "type__" in other:
            return cls._from_runtime(other)
        other = np.asanyarray(other, dtype=object)
        other = np.ndarray.view(other, Cell)
        for i, x in other._iterall():
            np.ndarray.__setitem__(other, i, MatlabType.from_any(x))
        return other

    @classmethod
    def from_iterable(cls, iterable) -> "Cell":
        """
        Return a 1D `Cell` that contains the input elements.

        `Cell(tuple[cells])` may combine its input into a cell array:

            `Cell([[1, 2], [3, 4]])` === Matlab's `{1 2; 3 4}`.

        This method ensures that we only create a cell at the first level:

            `Cell.from_iterable([[1, 2], [3, 4]])` === Matlab's `{{1 2} {3 4}}`
        """
        obj = Cell(len(iterable))
        for i, elem in enumerate(iterable):
            obj[i] = elem
        return obj

    def _as_runtime(self):
        if self.ndim == 1:
            return MatlabType._to_runtime(self.tolist())
        else:
            size = np.array([[*np.shape(self)]])
            data = np.ndarray.view(self, np.ndarray)
            data = np.reshape(data, [-1], order="F").tolist()
            data = MatlabType._to_runtime(data)
            return dict(type__='cell', size__=size, data__=data)

    @classmethod
    def _from_runtime(cls, objdict):
        if objdict['type__'] != 'cell':
            raise TypeError('objdict is not a cell')
        size = np.array(objdict['size__'], dtype=np.uint32).ravel()
        data = np.array(objdict['data__'], dtype=object)
        data = data.reshape(size)
        try:
            obj = data.view(Cell)
        except Exception:
            raise RuntimeError(
                f'Failed to construct Cell data:\n'
                f'  data={data}\n'
                f'  objdict={objdict}'
            )
        return MatlabType.from_any(obj)

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

    class ValuesView(ValuesView):

        def __init__(self, parent):
            self._parent = parent

        def __len__(self):
            return len(self._parent.as_dict().values())

        def __iter__(self):
            return iter(self._parent.as_dict().values())

        def __contains__(self, value):
            return value in self._parent.as_dict().values()

    class ItemsView(ItemsView):

        def __init__(self, parent):
            self._parent = parent

        def __len__(self):
            return len(self._parent.as_dict().items())

        def __iter__(self):
            return iter(self._parent.as_dict().items())

        def __contains__(self, item):
            return item in self._parent.as_dict().items()

    # --- magic --------------------------------------------------------

    def __len__(self):
        if self.ndim:
            return super(np.ndarray, self).__len__()
        else:
            return len(self.keys())

    def __contains__(self, key):
        if self.ndim:
            return super(np.ndarray, self).__contains__(key)
        else:
            return key in self.keys()

    def __iter__(self):
        if self.ndim:
            return super(np.ndarray, self).__iter__()
        else:
            return iter(self.keys())

    def __getitem__(self, key):
        # NOTE
        #   We only insert a DelayedArray if it is a completely new key.
        #   Otherwise the default value is [], as per matlab.
        isnewkey = key not in self.keys()
        for _, elem in self._iterall():
            elem.setdefault(
                key,
                self._DEFAULT() if isnewkey else
                DelayedArray(self)
            )
        return self.as_dict()[key]

    def __setitem__(self, key, value):
        if np.ndim(self) == 0:
            # Scalar array: assign value to the field
            if isinstance(value, unpack):
                if len(value.args) != 1:
                    raise ValueError("Cannot broadcast.")
                value = value.args[0]

            np.ndarray.item(self)[key] = MatlabType.from_any(value)

        elif isinstance(value, unpack):
            # Each element in the struct array is matched with an element
            # in the "unpack" array.
            value = np.broadcast_to(value, np.shape(self))
            for i, elem in self._iterall():
                elem[key] = MatlabType.from_any(value[i])

        else:
            # Assign the same value to all elements in the struct array.
            for _, elem in self._iterall():
                elem[key] = MatlabType.from_any(value)

    def __delitem__(self, key):
        if key not in self._allkeys():
            raise KeyError(key)
        for _, elem in self._iterall():
            if key in elem:
                elem.__delitem__(key)

    # --- mapping ------------------------------------------------------

    def keys(self):
        return self.KeysView(self)

    def items(self):
        return self.ItemsView(self)

    def values(self):
        return self.ValuesView(self)

    def setdefault(self, key, value):
        for _, elem in self._iterall():
            elem.setdefault(key, MatlabType.from_any(value))

    def update(self, other):
        if isinstance(other, Struct):
            other = np.broadcast_to(self)
            for i, elem in self._iterall():
                elem.update(MatlabType.from_any(other[i]))
        else:
            for _, elem in self._iterall():
                elem.update(MatlabType.from_any(other))


class Struct(_DictMixin, _WrappedArray):
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

    # Same point as for cells (see comment)
    _DEFAULT = classmethod(lambda cls: Array.from_any([]))

    # Value used to fill-in a newly allocated array -> dict
    def _EMPTY(self, n) -> np.ndarray:
        data = np.empty([n], dtype=dict)
        for i in range(n):
            data[i] = {}
        return data

    def __new__(cls, *args, **kwargs) -> "Struct":
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

        # Ths logic here is that we may end up with an array of arrays
        # of dict, because np.asarray([array, array]) returns an
        # array([array, array]) rather than a single deep array.
        # To circumvent this, we find elements that are arrays, convert
        # them to lists, and call asarray again.
        rebuild = False
        for i, _ in obj._iterall():
            # NOTE: we use _iterall (not _iterindex) to cover
            # the case of scalar (empty-shaped) struct.
            elem = arr.item() if i is Ellipsis else arr[i]
            if isinstance(elem, np.ndarray):
                tmp = np.ndarray.view(elem, dict, np.ndarray)
                if elem.ndim == 0:
                    tmp = tmp.item()
                else:
                    tmp = tmp.tolist()
                arr[i] = tmp
                rebuild = True
        if rebuild:
            # Recurse (we may have arrays of arrays of arrays...)
            return cls(arr, **kwargs)

        for i, _ in obj._iterall():
            elem = arr.item() if i is Ellipsis else arr[i]
            if not isinstance(elem, dict):
                raise TypeError("Cannot convert", obj, "to Struct.")

        if kwargs:
            obj.update(kwargs)
        return obj

    @classmethod
    def from_any(cls, other) -> "Struct":
        """
        Convert (nested) dict-like objects to struct.
        Convert (array of) dict-like objects to struct array.
        """
        if isinstance(other, dict) and "type__" in other:
            # matlab object
            return cls._from_runtime(other)
        if isinstance(other, np.ndarray):
            # ndarray[dict]
            dtype = np.ndarray.view(other, np.ndarray).dtype
            if dtype in (object, dict):
                other = np.ndarray.view(other, Struct)
        if not isinstance(other, Struct):
            other = Struct(other)
        # nested from_any
        for _, x in other._iterall():
            for k, v in x.items():
                x[k] = MatlabType.from_any(v)
        return other

    @classmethod
    def _from_runtime(cls, objdict: dict) -> "Struct":
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
        return MatlabType.from_any(obj)

    def _as_runtime(self) -> dict:
        size = np.array([[*np.shape(self)]])
        data = np.ndarray.view(self, np.ndarray)
        data = np.reshape(data, [-1], order="F")
        data = MatlabType._to_runtime(data)
        return dict(type__='structarray', size__=size, data__=data)

    @property
    def as_struct(self) -> "Struct":
        return self

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
        return {
            key: Cell.from_iterable([
                elem.get(key, self._DEFAULT()) for _, elem in self._iterall()
            ]).reshape(np.shape(self))
            for key in self._allkeys()
        }

    def _allkeys(self):
        # Return all keys present across all elements.
        # Keys are ordered by (1) element (2) within-element order
        mock = {}
        for _, elem in self._iterall():
            mock.update({key: None for key in elem.keys()})
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
        try:
            return _DictMixin.__getitem__(self, key)
        except KeyError as e:
            raise AttributeError(str(e))

    def __setattr__(self, key, value):
        try:
            return _DictMixin.__setitem__(self, key, value)
        except KeyError as e:
            raise AttributeError(str(e))

    def __delattr__(self, key):
        try:
            return _DictMixin.__delitem__(self, key)
        except KeyError as e:
            raise AttributeError(str(e))

    # -------
    # Delayed
    # -------

    def _finalize(self):
        for i, elem in self._iterall():
            if not isinstance(elem, dict):
                np.ndarray.__setitem__(self, i, {})
                continue
            for key, value in elem.items():
                if isinstance(value, AnyMatlabArray):
                    elem[key] = value._finalize()
                else:
                    elem[key] = MatlabType.from_any(elem[key])
        return self


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
