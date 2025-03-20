from .core import MatlabType
from .utils import _import_matlab


class Runtime:
    """Namespace that holds the matlab runtime. All methods are static."""

    _initialize = None
    _instance = None
    verbose = True

    @staticmethod
    def instance():
        if Runtime._instance is None:
            if Runtime.verbose:
                print('Initializing Matlab Runtime...')
            Runtime._import_initialize()
            Runtime._instance = Runtime._initialize()
        return Runtime._instance

    @staticmethod
    def call(fn, *args, **kwargs):
        (args, kwargs) = Runtime._process_argin(*args, **kwargs)
        res = Runtime.instance().mpython_endpoint(fn, *args, **kwargs)
        return Runtime._process_argout(res)

    @staticmethod
    def _process_argin(*args, **kwargs):
        to_runtime = MatlabType._to_runtime
        args = tuple(map(to_runtime, args))
        kwargs = dict(zip(kwargs.keys(), map(to_runtime, kwargs.values())))
        return args, kwargs

    @staticmethod
    def _process_argout(res):
        return MatlabType.from_any(res)

    @staticmethod
    def _import_initialize():
        # NOTE(YB)
        #   I moved the import within a function so that array wrappers
        #   can be imported and used even when matlab is not properly setup.
        if Runtime._initialize:
            return
        try:
            from spm._spm import initialize
            Runtime._initialize = initialize
        except ImportError as e:
            # ~~~ UNUSED ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # import os
            # installer_path = os.path.join(
            #     os.path.dirname(os.path.abspath(__file__)),
            #     '_spm',
            #     'resources',
            #     'RuntimeInstaller.install'
            # )
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            print(Runtime._help)
            raise e
        
        # Make sure matlab is imported
        _import_matlab()

    _help = """
    Failed to import spm._spm. This can be due to a failure to find Matlab
    Runtime. Please verify that Matlab Runtime is installed and its path is set.
    See https://www.mathworks.com/help/compiler/mcr-path-settings-for-run-time-deployment.html
    for instructions on how to setup the path.
    If the issue persists, please open an issue with the entire error
    message at https://github.com/spm/spm-python/issues.
    """

