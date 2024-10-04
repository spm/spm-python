from spm.__wrap__ import _Runtime


def spm_mci_gprior_deriv(*args, **kwargs):
  """  Gradient of Log Gaussian prior  
    FORMAT [j] = spm_mci_gprior_deriv (Pr,M)  
     
    Pr        parameters (vectorised and in M.V subspace)  
    M         model structure  
     
    j         gradient of log Gaussian prior  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_gprior_deriv.m)
  """

  return _Runtime.call("spm_mci_gprior_deriv", *args, **kwargs)
