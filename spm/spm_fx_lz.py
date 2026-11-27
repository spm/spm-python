from spm._runtime import Runtime


def spm_fx_lz(*args, **kwargs):
    r"""
      flow for Lorenz attractor  
        FORMAT [y] = spm_fx_lz(x,u,P)  
        x - state  
        u - input  
        P - parameters  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_fx_lz.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_fx_lz", *args, **kwargs)
