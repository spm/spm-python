from spm.__wrapper__ import Runtime


def spm_MH(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_MH.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_MH", *args, **kwargs)
