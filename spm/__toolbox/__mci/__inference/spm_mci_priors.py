from spm._runtime import Runtime


def spm_mci_priors(*args, **kwargs):
    r"""
      Quantities for computing log prior in subspace  
        FORMAT [M] = spm_mci_priors (M)  
         
        M.V               projection matrix  
        M.ipC             Inverse prior cov in reduced space  
        M.log_prior_t2    second term of log prior   
        M.Np              dimension of reduced space  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/inference/spm_mci_priors.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_priors", *args, **kwargs)
