from .core import MatlabType
from .utils import _import_matlab

class MatlabFunction(MatlabType):
    """
    Wrapper for matlab function handles.

    Example
    -------
    ```python
    times2 = Runtime.call("eval", "@(x) 2.*x")
    assert(time2(1) == 2)
    ```
    """

    def __init__(self, matlab_object):
        super().__init__()

        matlab = _import_matlab()
        if not isinstance(matlab_object, matlab.object):
            raise TypeError("Expected a matlab.object")
        
        self._matlab_object = matlab_object

    def _as_runtime(self):
        return self._matlab_object

    @classmethod
    def _from_runtime(cls, other):
        return cls(other)

    @classmethod
    def from_any(cls, other):
        if isinstance(other, MatlabFunction):
            return other
        return cls._from_runtime(other)

    def __call__(self, *args, **kwargs):
        from .runtime import Runtime
        return Runtime.call(self._matlab_object, *args, **kwargs)