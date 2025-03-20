import numpy as np

# If scipy is available, convert matlab sparse matrices scipy.sparse
# otherwise, convert them to dense numpy arrays
try:
    from scipy import sparse
except (ImportError, ModuleNotFoundError):
    sparse = None

# ----------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------

# We'll complain later if the runtime is not instantiated
def _import_matlab():
    try:
        import matlab
    except (ImportError, ModuleNotFoundError):
        matlab = None
    return matlab 


def _copy_if_needed(out, inp, copy=None) -> np.ndarray:
    """Fallback implementation for asarray(*, copy: bool)"""
    if (
        out is not None and
        isinstance(inp, np.ndarray) and
        np.ndarray.view(out, np.ndarray).data !=
        np.ndarray.view(inp, np.ndarray).data
    ):
        if copy:
            out = np.copy(out)
        elif copy is False:
            raise ValueError("Cannot avoid a copy")
    return out


def _spcopy_if_needed(out, inp, copy=None):
    """Fallback implementation for asarray(*, copy: bool)"""
    if (
        out is not None and
        isinstance(inp, sparse.sparray) and
        out.data.data != inp.data.data
    ):
        if copy:
            out = out.copy()
        elif copy is False:
            raise ValueError("Cannot avoid a copy")
    return out


def _matlab_array_types():
    """Return a mapping from matlab array type to numpy data dtype."""
    matlab = _import_matlab()
    if matlab:
        return {
            matlab.double:  np.float64,
            matlab.single:  np.float32,
            matlab.logical: np.bool,
            matlab.uint64:  np.uint64,
            matlab.uint32:  np.uint64,
            matlab.uint16:  np.uint16,
            matlab.uint8:   np.uint8,
            matlab.int64:   np.int64,
            matlab.int32:   np.int32,
            matlab.int16:   np.int16,
            matlab.int8:    np.int8,
        }
    else:
        return {}


def _empty_array():
    """Matlab's default cell/struct elements are 0x0 arrays."""
    from .array import Array
    return Array.from_shape([0, 0])
