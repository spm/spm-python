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
import itertools
import numpy as np


class MatlabClassWrapper:
    _subclasses = dict()

    def _as_matlab_object(self):
        return self._objdict

    @staticmethod
    def _from_matlab_object(objdict):
        if objdict['type__'] != 'object':
            raise TypeError('objdict does not contain an object')

        if objdict['class__'] in MatlabClassWrapper._subclasses.keys():
            obj = MatlabClassWrapper\
                ._subclasses[objdict['class__']](_objdict=objdict)
        else:
            warnings.warn(f'Unknown Matlab class: {objdict["class__"]}')
            obj = MatlabClassWrapper(_objdict=objdict)
        return obj

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
        if isinstance(arg, (MatlabClassWrapper, StructArray)):
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
            map(Runtime._cast_argin, kwargs.values()
                )))

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
                    out = MatlabClassWrapper._from_matlab_object(res)
                elif res['type__'] == 'structarray':
                    print()
                    out = StructArray._from_matlab_object(res)
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



class StructArray:
    def __init__(self, *structs):
        if len(structs) == 1:
            if isinstance(structs[0], Struct):
                structs = [structs[0]]
            else:
                if all(map(isinstance, structs[0],itertools.repeat(int))):
                    size = structs[0]
                    structs = np.fromiter(
                        map(
                            lambda i: dict(), range(np.prod(size))),
                        dtype=object).reshape(size)
                elif all(map(isinstance, structs[0], itertools.repeat(dict))):
                    structs = structs[0]
                elif isinstance(structs[0], np.ndarray) \
                        and all(map(isinstance, structs[0].flat, itertools.repeat(dict))):
                    structs = structs[0]
                else:
                    raise TypeError(f'arguments not understood: {structs}')

        if isinstance(structs, np.ndarray):
            structs = np.fromiter(
                map(dict, structs.flat),
                dtype=object).reshape(structs.shape)
        else:
            structs = np.fromiter(
                map(dict, structs),
                dtype=object)

        if len(structs.shape) == 1:
            structs = structs[:, None]

        self._structs = structs
        self._objdict = dict(
            type__='structarray',
            size__=np.array(structs.shape),
            data__=[]
        )

    def __getitem__(self, index):
        item = self._structs[index]
        return Struct(item)

    def keys(self):
        return set(
            itertools.chain.from_iterable(
                map(dict.keys, self._structs.flat)))

    def _as_matlab_object(self):
        _ = [*map(
            lambda arg: arg[0].__setitem__(arg[1], np.array([])),
            filter(
                lambda arg: arg[1] not in arg[0].keys(),
                itertools.product(self._structs.flat, self.keys())
            )
        )]
        objdict = self._objdict
        objdict['data__'] = self._structs.tolist()
        return objdict

    def __repr__(self):
        return self._structs \
            .__repr__() \
            .replace('array([], dtype=float64)', 'empty') \
            .replace('matlab.double([])', 'empty') \
            .replace('array(', 'StructArray(\n  data=') \
            .replace(', dtype=object', f',\n  keys={self.keys()}')

    @staticmethod
    def _from_matlab_object(objdict):
        if objdict['type__'] != 'structarray':
            raise TypeError('objdict is not a structarray')
        size = tuple(map(int, objdict['size__'][0]))
        data = np.fromiter(objdict['data__'], dtype=object)
        data = data.reshape(size)
        try:
            obj = StructArray(data)
        except Exception as e:
            raise RuntimeError(f'Failed to construct StructArray data:\n  data={data}\n  objdict={objdict}')

        return obj
