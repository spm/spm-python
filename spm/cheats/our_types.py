__all__ = ["asnum", "ascell", "asstruct"]
from spm.__wrapper__ import _MatlabTypeHelpers


asnum = _MatlabTypeHelpers._to_num
ascell = _MatlabTypeHelpers._to_cell
asstruct = _MatlabTypeHelpers._to_struct
