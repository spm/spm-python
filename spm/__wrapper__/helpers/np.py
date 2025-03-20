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


def base(array):
    """Equivalent to `array.base`."""
    return np.ndarray.view(array, np.ndarray).base


def data(array):
    """Equivalent to `array.data`."""
    return np.ndarray.view(array, np.ndarray).data


def dtype(array):
    """Equivalent to `array.dtype`."""
    return np.ndarray.view(array, np.ndarray).dtype


def flags(array):
    """Equivalent to `array.flags`."""
    return np.ndarray.view(array, np.ndarray).flags


def flat(array):
    """Equivalent to `array.flat`."""
    return np.ndarray.view(array, np.ndarray).flat


def strides(array):
    """Equivalent to `array.strides`."""
    return np.ndarray.view(array, np.ndarray).strides


def T(array):
    """Equivalent to `array.T`."""
    kls = type(array)
    return np.ndarray.view(array, np.ndarray).T.view(kls)


def mT(array):
    """Equivalent to `array.mT`."""
    kls = type(array)
    return np.ndarray.view(array, np.ndarray).mT.view(kls)


# -------
# methods
# -------


def dump(array, file):
    """Equivalent to `array.dump(file)`."""
    return np.ndarray.dump(array, file)


def dumps(array, file):
    """Equivalent to `array.dumps(file)`."""
    return np.ndarray.dumps(array, file)


def fill(array, value):
    """Equivalent to `array.fill(value)`."""
    return np.ndarray.fill(array, value)


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
