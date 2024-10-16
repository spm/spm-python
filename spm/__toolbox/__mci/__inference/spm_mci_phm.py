from spm.__wrapper__ import Runtime


def spm_mci_phm(*args, **kwargs):
  """  Compute Log Evidence using Posterior Harmonic Mean (PHM)  
    FORMAT [logev] = spm_mci_phm (L)  
     
    L          [S x 1] vector containing log-likelihood of samples  
    logev      log evidence from PHM  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_phm.m)
  """

  return Runtime.call("spm_mci_phm", *args, **kwargs)
