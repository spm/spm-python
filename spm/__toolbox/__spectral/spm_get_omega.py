from spm.__wrapper__ import Runtime


def spm_get_omega(*args, **kwargs):
    """
      Get expected error of MAR model  
        FORMAT [Omega] = spm_get_omega (p,d,w_cov,xtx)  
         
        p         Number of time lags  
        d         Dimension of time series  
        w_cov     Uncertainty in MAR coefficients  
        xtx       X'X where X is design matrix (ie. from lagged data)  
         
        Omega     Expected error  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/spectral/spm_get_omega.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_get_omega", *args, **kwargs)
