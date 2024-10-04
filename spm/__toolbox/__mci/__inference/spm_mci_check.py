from spm.__wrap__ import _Runtime


def spm_mci_check(*args, **kwargs):
  """  Check model structure M is correctly specified  
    FORMAT [corr] = spm_mci_check (M)  
     
    corr      1 for correctly specified model  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_check.m)
  """

  return _Runtime.call("spm_mci_check", *args, **kwargs)
