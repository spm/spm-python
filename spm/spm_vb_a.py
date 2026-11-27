from spm._runtime import Runtime


def spm_vb_a(*args, **kwargs):
    r"""
      Update AR coefficients in VB GLM-AR model   
        FORMAT [block] = spm_vb_a(Y,block)  
         
        Y      - [T x N] time series   
        block  - data structure (see spm_vb_glmar)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_vb_a.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_vb_a", *args, **kwargs)
