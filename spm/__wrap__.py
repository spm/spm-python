from spm._spm import initialize


class _MatlabClassWrapper:
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
		_MatlabClassWrapper._subclasses[cls.__name__] = cls


class _Runtime:
	_instance = None
	verbose = True

	@staticmethod
	def instance():
		if _Runtime._instance is None:
			if _Runtime.verbose: 
				print('Initializing Matlab Runtime...')
			_Runtime._instance = initialize()
		return _Runtime._instance

	@staticmethod
	def _register_class(classname, classtype): 
		_Runtime.classes[classname] = classtype

	@staticmethod
	def call(fn, *args, **kwargs): 
		[args, kwargs] = _Runtime._process_argin(*args, **kwargs) 
		res = _Runtime.instance().mpython_endpoint(fn, *args, **kwargs)
		return _Runtime._process_argout(res)

	@staticmethod
	def _cast_argin(arg):
		if isinstance(arg, _MatlabClassWrapper): 
				arg = arg._as_matlab_object()
		elif isinstance(arg, dict):
			_, arg = _Runtime._process_argin(**arg)
		elif isinstance(arg, (tuple, dict, list, set)):
			arg, _ = _Runtime._process_argin(*arg)
		return arg

	@staticmethod
	def _process_argin(*args, **kwargs):
		args = tuple(map(_Runtime._cast_argin, args))
		kwargs = dict(zip(
			kwargs.keys(), 
			map(_Runtime._cast_argin, kwargs.values()
				))) 

		return args, kwargs

	@staticmethod
	def _process_argout(res):
		out = res
		if isinstance(res, tuple): 
			out = tuple(_Runtime._process_argout(r) for r in res)
		else:
			if isinstance(res, dict): 
				if 'type__' in res.keys(): 
					if res['type__'] == 'object' and res['class__'] in _MatlabClassWrapper._subclasses.keys(): 
						out = _MatlabClassWrapper._subclasses[res['class__']]._from_matlab_object(res)

		return out

