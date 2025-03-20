from .base_types import (
    MatlabType, 
    AnyMatlabArray, 
)
from .delayed_types import (
    AnyDelayedArray,
    DelayedCell,
    DelayedStruct,
)
import numpy as np

# ----------------------------------------------------------------------
# WrappedArray
# ----------------------------------------------------------------------x
class AnyWrappedArray(AnyMatlabArray):
    """Base class for wrapped numpy/scipy arrays."""

    @classmethod
    def _parse_args(cls, *args, **kwargs):
        """
        This function is used in the `__new__` constructor of
        Array/Cell/Struct.

        It does some preliminary preprocesing to reduces the number of
        cases that must be handled by `__new__`.

        In particular:

        * It converts multiple integer arguments to a single list[int]
        * It extracts the shape or object to copy, if there is one.
        * It convert positional dtype/order into keywords.

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
    Base class for "arrays of things" (`Array`, `Cell`, `Struct`)
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
        """Resize array if needed, then fallback to `np.ndarray` indexing."""
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
        """Resize array if needed, then fallback to `np.ndarray` indexing."""
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
          raises `IndexError` (but instead returns the overlap between
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
        from ..cell import Cell
        from ..struct import Struct # FIXME: avoid circular import

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