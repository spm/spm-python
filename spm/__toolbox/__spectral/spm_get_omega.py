from spm._runtime import Runtime


def spm_get_omega(*args, **kwargs):
    r"""
      Get expected error of MAR model  
        FORMAT [Omega] = spm_get_omega (p,d,w_cov,xtx)  
         
        p         Number of time lags  
        d         Dimension of time series  
        w_cov     Uncertainty in MAR coefficients  
        xtx       X'X where X is design matrix (ie. from lagged data)  
         
        Omega     Expected error  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/spectral/spm_get_omega.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_get_omega", *args, **kwargs)
