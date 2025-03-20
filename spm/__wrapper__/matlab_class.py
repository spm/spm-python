from .core import MatlabType

import numpy as np
import warnings

class MatlabClass(MatlabType):
    _subclasses = dict()

    def __new__(cls, *args, _objdict=None, **kwargs):
        if _objdict is None:
            if cls.__name__ in MatlabClass._subclasses.keys():
                from .runtime import Runtime

                obj = Runtime.call(cls.__name__, *args, **kwargs)
            else:
                obj = super().__new__(cls)
        else:
            obj = super().__new__(cls)
            obj._objdict = _objdict
        return obj

    def __init_subclass__(cls):
        super().__init_subclass__()
        if hasattr(cls, 'subsref'):
            cls.__getitem__ = MatlabClass.__getitem
            cls.__call__ = MatlabClass.__call

        if hasattr(cls, 'subsasgn'):
            cls.__setitem__ = MatlabClass.__setitem

        MatlabClass._subclasses[cls.__name__] = cls

    @classmethod
    def from_any(cls, other):
        if isinstance(other, dict) and "type__" in other:
            return cls._from_runtime(other)
        if not isinstance(other, cls):
            raise TypeError(f"Cannot convert {type(other)} to {cls}")
        return other

    @classmethod
    def _from_runtime(cls, objdict):
        if objdict['class__'] in MatlabClass._subclasses.keys():
            obj = MatlabClass._subclasses[objdict['class__']](
                _objdict=objdict
            )
        else:
            warnings.warn(f'Unknown Matlab class type: {objdict["class__"]}')
            obj = MatlabClass(_objdict=objdict)
        return obj

    def _as_runtime(self):
        return self._objdict

    def __getattr(self, key):
        try:
            return self.subsref({'type': '.', 'subs': key})
        except Exception:
            raise AttributeError(key)

    def __getitem(self, ind):
        index = self._process_index(ind)
        try:
            return self.subsref({'type': '()', 'subs': index})
        except Exception:
            ...
        try:
            return self.subsref({'type': '{}', 'subs': index})
        except Exception:
            raise IndexError(index)

    def __setitem(self, ind, value):
        index = self._process_index(ind)
        try:
            return self.subsasgn({'type': '()', 'subs': index}, value)
        except Exception:
            ...
        try:
            return self.subsasgn({'type': '{}', 'subs': index}, value)
        except Exception:
            raise IndexError(index)

    def __call(self, *index):
        index = self._process_index(index)
        try:
            return self.subsref({'type': '{}', 'subs': index})
        except Exception:
            raise IndexError(index)

    def _process_index(self, ind, k=1, n=1):
        # FIXME: This should not need to call matlab
        try:
            return tuple(
                self._process_index(i, k+1, len(ind))
                for k, i in enumerate(ind)
            )
        except TypeError:
            pass
        
        from .runtime import Runtime

        if not hasattr(self, '__endfn'):
            self.__endfn = Runtime.call('str2func', 'end')

        def end():
            return Runtime.call(self.__endfn, self._as_runtime(), k, n)

        if isinstance(ind, int):
            if ind >= 0:
                index = ind + 1
            elif ind == -1:
                index = end()
            else:
                index = end() + ind - 1
        elif isinstance(ind, slice):
            if ind.start is None and ind.stop is None and ind.step is None:
                index = ':'
            else:
                if ind.start is None:
                    start = 1
                elif ind.start < 0:
                    start = end() + ind.start
                else:
                    start = ind.start + 1

                if ind.stop is None:
                    stop = end()
                elif ind.stop < 0:
                    stop = end() + ind.stop
                else:
                    stop = ind.stop + 1

                if ind.step is None:
                    step = 1
                else:
                    step = ind.step

                min_ = min(start, stop)
                max_ = max(start, stop)
                if step > 0:
                    index = np.arange(min_, max_, step)
                else:
                    index = np.arange(max_, min_, step)
        else:
            index = ind

        return index
