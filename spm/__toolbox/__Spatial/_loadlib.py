from spm.__wrapper__ import Runtime


def _loadlib(*args, **kwargs):
    """
      Load a shared library into MATLAB  
        FORMAT loadlib(nam)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Spatial/private/loadlib.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("loadlib", *args, **kwargs, nargout=0)
