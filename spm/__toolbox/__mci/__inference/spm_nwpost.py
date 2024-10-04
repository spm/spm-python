from spm.__wrap__ import _Runtime


def spm_nwpost(*args, **kwargs):
  """  Get posterior distribution over m,Lambda  
    FORMAT [M] = spm_nwpost (M,w)  
     
    M     M.prior - params of Normal-Wishart prior  
    w     Multivariate data samples  
     
    M     M.post - params of Normal-Wishart posterior  
     
    Bernardo and Smith, Bayesian Theory, 2000 (p.441)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_nwpost.m)
  """

  return _Runtime.call("spm_nwpost", *args, **kwargs)
