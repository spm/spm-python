from spm.__wrap__ import _Runtime


def spm_mci_diff(*args, **kwargs):
  """  Compute gradient and curvature of log likelihood using finite differences  
    FORMAT [dLdp,iCpY,L] = spm_mci_diff (P,M,U,Y)  
     
    dLdp      gradient of log likelihood  
    iCpY      curvature (observed Fisher Information)  
    L         log likelihood  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_diff.m)
  """

  return _Runtime.call("spm_mci_diff", *args, **kwargs)
