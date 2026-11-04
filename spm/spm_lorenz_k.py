from spm._runtime import Runtime


def spm_lorenz_k(*args, **kwargs):
    r"""
      Equations of motion for coupled Lorenz attractors  
        FORMAT [f] = spm_lorenz_k(x,v,P)  
        x - hidden states (3 x N)  
        v - exogenous input  
        P - parameters  
            P.t = N x 1  
            P.k = 1 x 1  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_lorenz_k.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_lorenz_k", *args, **kwargs)
