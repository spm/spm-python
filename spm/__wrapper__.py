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
