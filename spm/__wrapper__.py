from spm._spm import initialize


class MatlabClassWrapper:
	_subclasses = dict()

	def __init__(self, _objdict):
		self._objdict = _objdict

	@classmethod
	def _from_matlab_object(cls, res):
		return cls(_objdict=res)

	def _as_matlab_object(self): 
		return self._objdict

	def __init_subclass__(cls):
		super().__init_subclass__()
		MatlabClassWrapper._subclasses[cls.__name__] = cls
		if hasattr(cls, 'display'):
			cls.__repr__ = cls.display


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
		elif isinstance(arg, dict):
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
		else:
			if isinstance(res, dict): 
				if 'type__' in res.keys(): 
					if res['type__'] == 'object' and res['class__'] in MatlabClassWrapper._subclasses.keys(): 
						out = MatlabClassWrapper._subclasses[res['class__']]._from_matlab_object(res)

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
