from .core import (
    WrappedArray,
    _DictMixin,
    MatlabType,
    DelayedStruct
)
from .utils import (
    _copy_if_needed, 
    _empty_array
)

import numpy as np


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

    | | | | | | |
    |-|-|-|-|-|-|
    | `as`      | `assert`  | `break`   | `class`   | `continue`| `def`     |
    | `del`     | `elif`    | `else`    | `except`  | `False`   | `finally` |
    | `for`     | `from`    | `global`  | `if`      | `import`  | `in`      |
    | `is`      | `lambda`  | `None`    | `nonlocal`| `not`     | `or`      |
    | `pass`    | `raise`   | `return`  | `True`    | `try`     | `while`   |
    | `with`    | `yield`   |
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

            * `"C"` : row-major (C-style);
            * `"F"` : column-major (Fortran-style).

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

            * `"C"` : row-major (C-style);
            * `"F"` : column-major (Fortran-style);
            * `"A"` : (any) `"F"` if a is Fortran contiguous, `"C"` otherwise;
            * `"K"` : (keep) preserve input order;
            * `None`: preserve input order if possible, `"C"` otherwise.
        copy : bool | None, default=None
            Whether to copy the underlying data.

            * `True` : the object is copied;
            * `None` : the the object is copied only if needed;
            * `False`: raises a `ValueError` if a copy cannot be avoided.
        owndata : bool, default=None
            If `True`, ensures that the returned `Struct` owns its data.
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
        from .cell import Cell
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

        from .cell import Cell
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

