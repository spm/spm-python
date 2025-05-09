from mpython.runtime import Runtime as RuntimeBase


class Runtime(RuntimeBase):
    """
    Runtime specialization that imports the correct CTF.
    """

    @classmethod
    def _import_runtime(cls):
        import spm_runtime
        return spm_runtime


class RuntimeMixin:
    """
    Mixin that SPM classes must inherit so that they can call the
    correct runtime.
    """

    @classmethod
    def _runtime(cls):
        return Runtime
