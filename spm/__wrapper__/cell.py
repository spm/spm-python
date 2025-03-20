from .core import (
    MatlabType,
    WrappedArray,
    DelayedCell,
    AnyDelayedArray,
    _ListMixin,
)
from .utils import (
    _empty_array, 
    _copy_if_needed, 
    _import_matlab, 
    _matlab_array_types
)
global matlab

import numpy as np


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

            * `"C"` : row-major (C-style);
            * `"F"` : column-major (Fortran-style).

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
        owndata : bool, default=False
            If `True`, ensures that the returned `Cell` owns its data.
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
