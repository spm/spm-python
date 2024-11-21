from spm.__wrapper__ import Runtime


def spm_mci_phm(*args, **kwargs):
    """
      Compute Log Evidence using Posterior Harmonic Mean (PHM)  
        FORMAT [logev] = spm_mci_phm (L)  
         
        L          [S x 1] vector containing log-likelihood of samples  
        logev      log evidence from PHM  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_phm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_phm", *args, **kwargs)
