from .base_types import MatlabType
from .wrapped_types import WrappedArray
from .delayed_types import AnyDelayedArray
from ..utils import _matlab_array_types, _empty_array

import numpy as np
from collections.abc import (
    MutableSequence, 
    MutableMapping, 
    KeysView, 
    ValuesView, 
    ItemsView
)

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
    def _from_runtime(cls, dictobj: dict):
        if dictobj['type__'] != 'sparse':
            raise ValueError("Not a matlab sparse matrix")
        size = np.array(dictobj['size__'], dtype=np.uint64).ravel()
        size = size.tolist()
        dtype = _matlab_array_types()[type(dictobj['values__'])]
        indices = np.asarray(dictobj['indices__'], dtype=np.long) - 1
        values = np.asarray(dictobj['values__'], dtype=dtype).ravel()
        return cls.from_coo(values, indices.T, size)
    

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

            from ..struct import Struct # FIXME: circular imports
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
        from ..struct import Struct # FIXME: circular imports
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
    class deal: # FIXME: Removed dependency to Cell
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

        def broadcast_to_struct(self, struct):
            shape = struct.shape + self.shape[len(struct.shape):]
            return np.broadcast_to(self, shape)

        def to_cell(self):
            from ..cell import Cell # FIXME: circular imports
            return np.ndarray.view(self, Cell)

