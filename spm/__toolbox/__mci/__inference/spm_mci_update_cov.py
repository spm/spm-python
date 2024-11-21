from spm.__wrapper__ import Runtime


def spm_mci_update_cov(*args, **kwargs):
    """
      Update covariance matrix of proposal density using Robbins-Monro  
        FORMAT [P] = spm_mci_update_cov (P)  
         
        See e.g.  
        H. Haario, E. Saksman, and J. Tamminen. An adaptive Metropolis algorithm.   
        Bernoulli, 7(2):223-242, 2001.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_update_cov.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_update_cov", *args, **kwargs)
