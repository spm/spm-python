from spm._runtime import Runtime


def spm_ness_cond_inv(*args, **kwargs):
    r"""
      Returns polynomial parameterisation (sP)of a Gaussian density  
        FORMAT [Sp,o] = spm_ness_cond_inv(m,C)  
       --------------------------------------------------------------------------  
        m  - mean  
        C  - covariance  
         
        Sp - Polynomial coefficients; i.e., parameters of log density  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_ness_cond_inv.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ness_cond_inv", *args, **kwargs)
