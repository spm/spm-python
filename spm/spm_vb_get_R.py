from spm._runtime import Runtime


def spm_vb_get_R(*args, **kwargs):
    r"""
      Get posterior correlation matrix for regression coefficients  
        FORMAT [R] = spm_vb_get_R(slice,h0)  
          
        slice  - data structure (see spm_vb_glmar)  
          
        R      - posterior correlation matrix of regression coefficients  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_vb_get_R.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_vb_get_R", *args, **kwargs)
