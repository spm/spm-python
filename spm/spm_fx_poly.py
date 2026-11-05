from spm._runtime import Runtime


def spm_fx_poly(*args, **kwargs):
    r"""
      Normal (bilinear) form equation of motion  
        FORMAT [f] = spm_fx_poly(x,v,P)  
        x      - state vector  
        v      - exogenous cause  
        P      - free parameters  
         
        f      - dx/dt  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_fx_poly.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_fx_poly", *args, **kwargs)
