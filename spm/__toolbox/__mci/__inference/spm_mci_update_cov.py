from spm.__wrap__ import _Runtime


def spm_mci_update_cov(*args, **kwargs):
  """  Update covariance matrix of proposal density using Robbins-Monro  
    FORMAT [P] = spm_mci_update_cov (P)  
     
    See e.g.  
    H. Haario, E. Saksman, and J. Tamminen. An adaptive Metropolis algorithm.   
    Bernoulli, 7(2):223-242, 2001.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_update_cov.m)
  """

  return _Runtime.call("spm_mci_update_cov", *args, **kwargs)
