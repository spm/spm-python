from spm._runtime import Runtime


def FIN_TEST(*args, **kwargs):
    r"""
      Iterated simulations  
        FORMAT FIN_TEST  
       --------------------------------------------------------------------------  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/FIN_TEST.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("FIN_TEST", *args, **kwargs, nargout=0)
