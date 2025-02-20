"""
Struct cannot expose np.ndarray attributes/methods, as they may conflict
with its keys.

This module implements external functions to access these attributes.

Some attributes/methods do not need to be implemented here, as they
already exist in the numpy namespace. Examples include:

* `np.ndim`
* `np.shape`
* `np.size`
* `np.reshape`
* `np.squeeze`
* `np.copy`
* `np.ravel`

as well as all math functions (`np.sum`, `np.mean`, etc.)
"""
import numpy as np


# ----------
# properties
# ----------


def dtype(array):
    """Equivalent to `array.dtype`."""
    return np.asarray(array).dtype


def flat(array):
    """Equivalent to `array.flat`."""
    return np.asarray(array).flat


def strides(array):
    """Equivalent to `array.strides`."""
    return np.asarray(array).strides


def T(array):
    """Equivalent to `array.T`."""
    kls = type(array)
    return np.asarray(array).T.view(kls)


# -------
# methods
# -------


def flatten(array):
    """Equivalent to `array.flatten()`."""
    return np.ndarray.flatten(array)


def item(array):
    """Equivalent to `array.item()`."""
    return np.ndarray.item(array)


def resize(array, *new_shape, **kwargs) -> None:
    """Equivalent to `array.resize(*new_shape)`."""
    np.ndarray.resize(array, *new_shape, **kwargs)


def tolist(array):
    """Equivalent to `array.tolist()`."""
    return np.ndarray.tolist(array)
