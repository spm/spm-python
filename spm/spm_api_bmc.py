from spm.__wrapper__ import Runtime


def spm_api_bmc(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_api_bmc.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_api_bmc", *args, **kwargs)
