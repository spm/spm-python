from spm._runtime import Runtime


def spm_vb_gamma(*args, **kwargs):
    r"""
      Variational Bayes for GLMAR model - Update gamma and get w_dev, wk_mean  
        FORMAT [block] = spm_vb_gamma(Y,block)  
         
        Y      - [T x N] time series  
        block  - data structure (see spm_vb_glmar)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_vb_gamma.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_vb_gamma", *args, **kwargs)
