from spm._runtime import Runtime


def ADEM_lorenz_surprise(*args, **kwargs):
    r"""
      This demo computes the cost-function (negative reward) for a Lorenz  
        system; to show cost can be computed easily from value (negative   
        surprise or sojourn time). However, value is not a Lyapunov function  
        because the flow is not curl-free (i.e., is not irrotational).  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/ADEM_lorenz_surprise.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ADEM_lorenz_surprise", *args, **kwargs, nargout=0)
