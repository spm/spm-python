__all__ = ["np", "matlab", "asnum", "ascell", "asstruct"]

from . import np
from . import matlab


from spm.__wrapper__ import Array, Cell, Struct
asnum = Array.from_any
ascell = Cell.from_any
asstruct = Struct.from_any
