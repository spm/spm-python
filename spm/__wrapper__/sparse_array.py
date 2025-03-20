from .core import (
    AnyWrappedArray, 
    _SparseMixin
)
from .utils import (
    _spcopy_if_needed,
    sparse
)
from .array import Array

import numpy as np
import warnings

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

