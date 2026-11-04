from spm._runtime import Runtime


def spm_mci_phm(*args, **kwargs):
    r"""
      Compute Log Evidence using Posterior Harmonic Mean (PHM)  
        FORMAT [logev] = spm_mci_phm (L)  
         
        L          [S x 1] vector containing log-likelihood of samples  
        logev      log evidence from PHM  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/inference/spm_mci_phm.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_phm", *args, **kwargs)
