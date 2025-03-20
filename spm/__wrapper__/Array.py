from .core import (
    WrappedArray, 
    _ListishMixin
)
from .utils import _copy_if_needed

import numpy as np


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

            * "C" : row-major (C-style);
            * "F" : column-major (Fortran-style).

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
            If `True`, ensures that the returned `Array` owns its data.
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
    def from_cell(cls, other, **kwargs) -> "Array":
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

            * `"C"` : row-major (C-style);
            * `"F"` : column-major (Fortran-style);
            * `"A"` : (any) `"F"` if a is Fortran contiguous, `"C"` otherwise;
            * `"K"` : (keep) preserve input order.
        owndata : bool, default=None
            If `True`, ensures that the returned `Array` owns its data.
            This may trigger an additional copy.

        Returns
        -------
        array : Array
            Converted array.
        """
        from .cell import Cell # FIXME: avoid circular import

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