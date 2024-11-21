from spm.__wrapper__ import Runtime


def spm_mci_priors(*args, **kwargs):
    """
      Quantities for computing log prior in subspace  
        FORMAT [M] = spm_mci_priors (M)  
         
        M.V               projection matrix  
        M.ipC             Inverse prior cov in reduced space  
        M.log_prior_t2    second term of log prior   
        M.Np              dimension of reduced space  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_priors.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_priors", *args, **kwargs)
