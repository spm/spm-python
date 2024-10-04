from spm.__wrap__ import _Runtime


def spm_phi(*args, **kwargs):
  """  Logistic function  
    FORMAT [y] = spm_phi(x)  
     
    y   = 1./(1 + exp(-x))  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_phi.m)
  """

  return _Runtime.call("spm_phi", *args, **kwargs)
