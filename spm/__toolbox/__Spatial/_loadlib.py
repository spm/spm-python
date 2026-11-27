from spm._runtime import Runtime


def _loadlib(*args, **kwargs):
    r"""
      Load a shared library into MATLAB  
        FORMAT loadlib(nam)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Spatial/private/loadlib.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("loadlib", *args, **kwargs, nargout=0)
