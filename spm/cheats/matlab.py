__all__ = [
    'num2cell',
    'cell2num',
    'struct2cell',
    'cell2struct',
]
import numpy as np

from spm.__wrapper__ import Cell, Array, Struct


def num2cell(array):
    """
    Convert an `Array` to a `Cell`.
    """
    # TODO: check that the python and matlab's versions have equivalent bhv
    obj = np.asanyarray(array, dtype=object)
    return np.ndarray.view(obj, Cell)


def cell2num(cell, dtype=None):
    """
    Convert a `Cell` to an `Array`.
    """
    # TODO: check that the python and matlab's versions have equivalent bhv
    obj = np.asanyarray(cell.tolist(), dtype=dtype)
    return np.ndarray.view(obj, Array)


def struct2cell(struct):
    """
    Convert a `Struct` to a `Cell`.
    The output cell contains the struct's values (not the keys).
    """
    # TODO: check that the python and matlab's versions have equivalent bhv
    obj = np.stack([struct[key] for key in struct.keys()])
    return np.ndarray.view(obj, Cell)


def cell2struct(cell):
    """
    Convert a `Cell` of `Struct` into a `Struct`.
    """
    # TODO: check that the python and matlab's versions have equivalent bhv
    obj = np.empty(cell.shape, dtype=dict)
    for i, x in cell._iterall():
        obj[i] = x
    return np.ndarray.view(obj, Struct)
