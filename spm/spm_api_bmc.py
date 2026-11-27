from spm._runtime import Runtime


def spm_api_bmc(*args, **kwargs):
    r"""
      API to select and compare DCMs using Bayesian model comparison  
        FORMAT out=spm_api_bmc(F,N,alpha,exp_r,xp)  
         
        INPUT:  
        F      - Matrix/Vector of log model evidences  
        N      - vector of model names  
        alpha  - vector of model probabilities  
        exp_r  - expectation of the posterior p(r|y)  
        xp     - exceedance probabilities  
         
        OUTPUT:  
        out    - conditional probability of DCMs (when using fixed effect method)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_api_bmc.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_api_bmc", *args, **kwargs)
