from mpython import Runtime


def _loadlib(*args, **kwargs):
    """
      Load a shared library into MATLAB
        FORMAT loadlib(nam)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Spatial/private/loadlib.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("loadlib", *args, **kwargs, nargout=0)
