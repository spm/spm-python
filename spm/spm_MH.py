from spm._runtime import Runtime


def spm_MH(*args, **kwargs):
    r"""
      The Rejection-Metropolis-Hastings Algorithm  
        FORMAT [P,F] = spm_MH(L,B,y,M)  
         
        L   - likelihood function: inline(P,y,M)  
        B   - free parameter [structure]  
        Y   - response  [structure]  
        M   - model [structure]  
         
        P   - Sample from posterior p(P|y,M)  
        F   - marginal likelihood p(y|M) using harmonic mean  
       --------------------------------------------------------------------------  
         
        Returns a harmonic mean estimate of the log-marginal likelihood or  
        log-evidence and a sample from the posterior density of the free  
        parameters of a model.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_MH.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_MH", *args, **kwargs)
