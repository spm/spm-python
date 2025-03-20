from .base_types import AnyMatlabArray
from ..utils import _empty_array
from ..exceptions import IndexOrKeyOrAttributeError

import numpy as np


class AnyDelayedArray(AnyMatlabArray):
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
    we cannot differentiate `a{x}.b = y` — where `a` is a cell that contains
    a struct — from `a(x).b = y` — where `a` is a struct array.

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
    * an `Array` (in the "set" context `a[x] = y`, when `y` is neither a
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

    _ATTRIBUTES = ("_parent", "_index", "_future", "_finalized")

    def __init__(self, parent, *index):
        """
        Parameters
        ----------
        parent : ndarray | dict
            Reference to the object that will eventually contain
            this element.

            * If the containing array is a `Cell`, `parent` should be a
              `ndarray` view of that cell, and `index` should be a
              [tuple of] int.
            * If the containing array is a `Struct`, `parent` should be a
              `dict`, and `index` should be a string.
        index : str | [tuple of] int
            Index into the parent where this element will be inserted.
        """
        super().__init__()
        self._parent = parent       # reference to parent container
        self._index = index         # index into parent container
        self._future = None         # future array
        self._finalized = False     # whether this array has been finalized

    @property
    def _final(self):
        self._finalize()
        return self._future

    def _finalize(self):
        if self._finalized:
            return

        if self._future is None:
            # FIXME: I am not entirely sure this should ever happen
            self._future = _empty_array()

        # if future array is wrapped, unwrap it
        if isinstance(self._future, WrappedDelayedArray):
            self._future = self._future._future
            if hasattr(self._future, "_delayed_wrapper"):
                del self._future._delayed_wrapper

        # set value in parent
        parent = self._parent
        for index in self._index[:-1]:
            parent = parent[index]
        parent[self._index[-1]] = self._future

        # finalize parent if needed
        if hasattr(self._parent, "_final"):
            self._parent = self._parent._final

        self._finalized = True

    def _error_is_not_finalized(self, *args, **kwargs):
        raise IndexOrKeyOrAttributeError(
            "This DelayedArray has not been finalized, and you are "
            "attempting to use it in a way that may break its finalization "
            "cycle. It most likely means that you are indexing out-of-bounds "
            "without *setting* the out-of-bound value. "
            "Correct usage: `a.b(i).c = x` | Incorrect usage: `x = a.b(i).c`."
        )

    # Kill all operators
    __str__ = __repr__ = _error_is_not_finalized
    __bool__ = __float__ = __int__ = _error_is_not_finalized
    __ceil__ = __floor__ = __round__ = __trunc__ = _error_is_not_finalized
    __add__ = __iadd__ = __radd__ = _error_is_not_finalized
    __sub__ = __isub__ = __rsub__ = _error_is_not_finalized
    __mul__ = __imul__ = __rmul__ = _error_is_not_finalized
    __truediv___ = __itruediv___ = __rtruediv___ = _error_is_not_finalized
    __floordiv___ = __ifloordiv___ = __rfloordiv___ = _error_is_not_finalized
    __eq__ = __ne__ = _error_is_not_finalized
    __gt__ = __ge__ = __lt__ = __le__ = _error_is_not_finalized
    __abs__ = __neg__ = __pos__ = _error_is_not_finalized
    __pow__ = __ipow__ = __rpow__ = _error_is_not_finalized
    __mod__ = __imod__ = __rmod__ = _error_is_not_finalized
    __divmod__ = __idivmod__ = __rdivmod__ = _error_is_not_finalized
    __contains__ = _error_is_not_finalized

    def __getattribute__(self, name):
        # Do not allow any attribute to be accessed except for those
        # explicitly allowed by the AnyDelayedArray class.
        # This is so no "computation" is peformed on DelayedCell,
        # DelayedStruct, etc.
        if name.startswith("_"):
            return super().__getattribute__(name)
        if name not in self.__dict__ and name not in AnyDelayedArray.__dict__:
            return self._error_is_not_finalized()
        return super().__getattribute__(name)

    # --- Promise type -------------------------------------------------

    @property
    def as_cell(self) -> "DelayedCell":
        if self._future is None:
            self._future = DelayedCell((), self._parent, *self._index)
        if not isinstance(self._future, DelayedCell):
            raise TypeError(
                f"{type(self._future)} cannot be interpreted as a Cell"
            )
        return self._future

    @property
    def as_struct(self) -> "DelayedStruct":
        if self._future is None:
            self._future = DelayedStruct((), self._parent, *self._index)
        if not isinstance(self._future, DelayedStruct):
            raise TypeError(
                f"{type(self._future)} cannot be interpreted as a Struct"
            )
        return self._future

    @property
    def as_num(self) -> "DelayedArray":
        if self._future is None:
            self._future = DelayedArray([0], self._parent, *self._index)
        if not isinstance(self._future, DelayedArray):
            raise TypeError(
                f"{type(self._future)} cannot be interpreted as a Array"
            )
        return self._future

    def as_obj(self, obj):
        from ..matlab_class import MatlabClass
        if (
            self._future is not None and
            not isinstance(self._future, MatlabClass)
        ):
            raise TypeError(
                f"{type(self._future)} cannot be interpreted as a {type(obj)}"
            )
        self._future = obj
        return self._future

    # --- Guess promised type ------------------------------------------

    def __call__(self, *index):
        return self.as_cell(*index)

    def __getitem__(self, index):
        return self.as_struct[index]

    def __getattr__(self, key):
        return self.as_struct[key]

    def __setitem__(self, index, value):
        from ..matlab_class import MatlabClass
        from ..cell import Cell
        from ..struct import Struct
        from ..array import Array

        if isinstance(index, str):
            arr = self.as_struct

        elif isinstance(value, MatlabClass):
            if index not in (0, -1):
                raise NotImplementedError(
                    "Implicit advanced indexing not implemented for",
                    type(value)
                )
            self.as_obj(value)
            return self._finalize()

        elif isinstance(value, (dict, Struct)):
            arr = self.as_struct
        elif isinstance(value, (tuple, list, set, Cell)):
            arr = self.as_cell
        elif isinstance(value, (int, float, np.number, Array)):
            arr = self.as_num
        elif isinstance(value, np.ndarray):
            if issubclass(value.dtype.type, np.number):
                arr = self.as_num
            else:
                arr = self.as_cell
        else:
            arr = self.as_cell

        arr[index] = value
        return self._finalize()  # Setter -> we can trigger finalize

    def __setattr__(self, key, value):
        if key in type(self)._ATTRIBUTES:
            return super().__setattr__(key, value)
        self.as_struct[key] = value
        return self._finalize()  # Setter -> we can trigger finalize

class WrappedDelayedArray(AnyDelayedArray):
    """
    Base class for future objects with known type.

    See `DelayedStruct`, `DelayedCell`, `DelayedArray`.
    """

    def __init__(self, future, parent, *index):
        """
        Parameters
        ----------
        future : Struct | Cell | Array
            Concrete object that will be inserted in the parent later.
        parent : Struct | Cell | AnyDelayedArray
            Parent object that contains the future object.
        *index : int | str
            Index of the future obect in its parent.
        """
        super().__init__(parent, *index)
        self._future = future

    def __call__(self, *index):
        return self._future.__call__(*index)

    def __getitem__(self, index):
        return self._future.__getitem__(index)

    def __getattr__(self, key):
        return self._future.__getattr__(key)

    def __setitem__(self, index, value):
        self._future.__setitem__(index, value)
        self._finalize()

    def __setattr__(self, key, value):
        if key in type(self)._ATTRIBUTES:
            return super().__setattr__(key, value)
        self._future.__setattr__(key, value)
        self._finalize()


class DelayedStruct(WrappedDelayedArray):
    """
    A `Struct` that will insert itself in its parent later.

    See `AnyDelayedArray`.
    """

    def __init__(self, shape, parent, *index):
        """
        Parameters
        ----------
        shape : list[int]
            Shape of the future struct array.
        parent : Struct | Cell | AnyDelayedArray
            Parent object that contains the future object.
        *index : int | str
            Index of the future object in its parent.
        """
        from ..struct import Struct
        future = Struct.from_shape(shape)
        future._delayed_wrapper = self
        super().__init__(future, parent, *index)


class DelayedCell(WrappedDelayedArray):
    """
    A `Cell` that will insert itself in its parent later.

    See `AnyDelayedArray`.
    """

    def __init__(self, shape, parent, *index):
        """
        Parameters
        ----------
        shape : list[int]
            Shape of the future cell array.
        parent : Struct | Cell | AnyDelayedArray
            Parent object that contains the future object.
        *index : int | str
            Index of the future object in its parent.
        """
        from ..cell import Cell
        future = Cell.from_shape(shape)
        future._delayed_wrapper = self
        super().__init__(future, parent, *index)

        # Insert delayed arrays instead of the usual defaults
        opt = dict(
            flags=['refs_ok', 'zerosize_ok', 'multi_index'],
            op_flags=['writeonly', 'no_broadcast']
        )
        arr = np.ndarray.view(self._future, np.ndarray)
        with np.nditer(arr, **opt) as iter:
            for elem in iter:
                elem[()] = AnyDelayedArray(self, iter.multi_index)


class DelayedArray(WrappedDelayedArray):
    """
    An `Array` that will insert itself in its parent later.

    See `AnyDelayedArray`.
    """

    def __init__(self, shape, parent, *index):
        """
        Parameters
        ----------
        shape : list[int]
            Shape of the future numeric array.
        parent : Struct | Cell | AnyDelayedArray
            Parent object that contains the future object.
        *index : int | str
            Index of the future object in its parent.
        """
        from ..array import Array
        future = Array.from_shape(shape)
        future._delayed_wrapper = self
        super().__init__(future, parent, *index)
