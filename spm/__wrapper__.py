try:
    from spm._spm import initialize
except ImportError as e:
    import os
    installer_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '_spm',
        'resources',
        'RuntimeInstaller.install')

    print("Failed to import, install Matlab Runtime and setup library path. ")
    print(f"Matlab Runtime installer can be found in: {installer_path}")
    raise e
import warnings


def _process_index(s):
    try:
        return [*map(_process_index, s)]
    except TypeError:
        pass

    if not isinstance(s, slice):
        return s

    if s.start is None and s.stop is None and s.step is None:
        return ':'
    else:
        if s.start is None:
            start = f'1'
        else:
            assert (s.start >= 0)
            start = f'{s.start + 1}'
        if s.stop is None:
            stop = 'end'
        elif s.stop >= 0:
            stop = f'{s.stop + 1}'
        elif s.stop < 0:
            stop = f'end-{abs(s.stop)}'
        if s.step is None or s.step == 1:
            step = ':'
        else:
            step = f':{s.step}:'
    return start + step + stop


class MatlabClassWrapper:
    _subclasses = dict()

    def _as_matlab_object(self):
        return self._objdict

    def __init_subclass__(cls):
        super().__init_subclass__()
        MatlabClassWrapper._subclasses[cls.__name__] = cls

    def __new__(cls, *args, _objdict=None, **kwargs):
        if _objdict is None:
            if cls.__name__ in MatlabClassWrapper._subclasses.keys():
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
            cls.__getitem__ = MatlabClassWrapper.__getitem
            cls.__call__    = MatlabClassWrapper.__call

        if hasattr(cls, 'subsasgn'):
            cls.__setitem__ = MatlabClassWrapper.__setitem

        MatlabClassWrapper._subclasses[cls.__name__] = cls

    def __getattr(self, key):
        try:
            return self.subsref({'type': '.', 'subs': key})
        except:
            raise AttributeError(key)

    def __getitem(self, index):
        index = _process_index(index)

        try:
            return self.subsref({'type': '()', 'subs': index})
        except:
            pass
        try:
            return self.subsref({'type': '{}', 'subs': index})
        except:
            raise IndexError(index)

    def __setitem(self, index, value):
        index = _process_index(index)

        try:
            return self.subsasgn({'type': '()', 'subs': index}, value)
        except:
            pass
        try:
            return self.subsasgn({'type': '{}', 'subs': index}, value)
        except:
            raise IndexError(index)

    def __call(self, *index):
        index = _process_index(index)
        try:
            return self.subsref({'type': '{}', 'subs': index})
        except:
            raise IndexError(index)



class Runtime:
    _instance = None
    verbose = True

    @staticmethod
    def instance():
        if Runtime._instance is None:
            if Runtime.verbose:
                print('Initializing Matlab Runtime...')
            Runtime._instance = initialize()
        return Runtime._instance

    @staticmethod
    def call(fn, *args, **kwargs):
        [args, kwargs] = Runtime._process_argin(*args, **kwargs)
        res = Runtime.instance().mpython_endpoint(fn, *args, **kwargs)
        return Runtime._process_argout(res)

    @staticmethod
    def _cast_argin(arg):
        if isinstance(arg, MatlabClassWrapper):
            arg = arg._as_matlab_object()
        if isinstance(arg, dict):
            _, arg = Runtime._process_argin(**arg)
        elif isinstance(arg, (tuple, dict, list, set)):
            arg, _ = Runtime._process_argin(*arg)
        return arg

    @staticmethod
    def _process_argin(*args, **kwargs):
        args = tuple(map(Runtime._cast_argin, args))
        kwargs = dict(zip(
            kwargs.keys(),
            map(Runtime._cast_argin, kwargs.values())))

        return args, kwargs

    @staticmethod
    def _process_argout(res):
        out = res
        if isinstance(res, tuple):
            out = tuple(Runtime._process_argout(r) for r in res)
        elif isinstance(res, list):
            out = list(Runtime._process_argout(r) for r in res)
        elif isinstance(res, dict):
            res = dict(zip(res.keys(), map(Runtime._process_argout, res.values())))
            if 'type__' in res.keys():
                if res['type__'] == 'object':
                    if res['class__'] in MatlabClassWrapper._subclasses.keys():
                        out = MatlabClassWrapper._subclasses[res['class__']](_objdict=res)
                    else:
                        warnings.warn(f'Unknown Matlab class type: {res["type__"]}')
                        out = MatlabClassWrapper(_objdict=res)
                else:
                    out = res
            else:
                out = Struct(**res)
        return out


class Struct(dict):
    """emulates struct with a dot.notation access to dictionary attributes"""
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class Cell(list):
    """emulates matlab's cell"""
    def __init__(self, m, n):
        super().__init__([[] for j in range(n)] for i in range(m))

    def __getitem__(self, index):
        if isinstance(index, tuple):
            i, j = index
            return self[i][j]
        else:
            return super().__getitem__(index)

    def __setitem__(self, index, value):
        if isinstance(index, tuple):
            i, j = index
            xi = self[i]
            xi[j] = value
            self[i] = xi
        else:
            super().__setitem__(index, value)
