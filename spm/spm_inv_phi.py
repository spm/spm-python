from spm.__wrap__ import _Runtime


def spm_inv_phi(*args, **kwargs):
  """  Inverse logistic function  
    FORMAT [y] = spm_inv_phi(x)  
     
    x   = log((y./(1 - y))  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_inv_phi.m)
  """

  return _Runtime.call("spm_inv_phi", *args, **kwargs)
