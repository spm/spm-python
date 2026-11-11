from spm._runtime import Runtime


def spm_MH_reml(*args, **kwargs):
    r"""
      Estimation of covariance components from y*y' using sampling  
        FORMAT [F,P] = spm_MH_reml(YY,X,Q,N,[hE]);  
         
        YY  - (m x m) sample covariance matrix Y*Y'  {Y = (m x N) data matrix}  
        X   - (m x p) design matrix  
        Q   - {1 x q} covariance components  
        N   - number of samples  
         
        hE  - prior expectation: log-normal hyper-parameterisation (with hyperpriors)  
         
        F   - [-ve] free energy F = log evidence = p(Y|X,Q)  
        P   - sample of hyperparameters from their posterior p(h|YY,X,Q)  
       --------------------------------------------------------------------------  
         
        This routine is using MCMC sampling (reverible Metropolis-Hastings)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_MH_reml.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_MH_reml", *args, **kwargs)
