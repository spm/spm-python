from spm._runtime import Runtime


def spm_mvb_bmc(*args, **kwargs):
    r"""
      Multivariate Bayesian model comparison (Baysian decoding of a contrast)  
        FORMAT [F,P,MVB] = spm_mvb_bmc(mvb)  
         
        mvb   : models to compare (file names)  
        F     : F ratio relative to null  
        P     : P-value relative to null  
        MVB   : best model  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_mvb_bmc.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mvb_bmc", *args, **kwargs)
