from spm._runtime import Runtime


def spm_mci_random(*args, **kwargs):
    r"""
      Random effects estimation  
        FORMAT [S] = spm_mci_random (mcmc,R,v,M,U,Y)  
         
        mcmc  Sampling parameters  
        R     Priors on random effects (R.pE, R.pC)  
        v     Fixed effects  
        M     Model Structure (single subject)  
        U     Inputs (single subject)  
        Y     Data (single subject)  
         
        S     Samples, [maxits x M.n]   
         
        Uses Langevin Monte Carlo  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/inference/spm_mci_random.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_random", *args, **kwargs)
