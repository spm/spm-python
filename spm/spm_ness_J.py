from spm.__wrap__ import _Runtime


def spm_ness_J(*args, **kwargs):
  """  Return the Jacobian given a polynomial parameterisation  
    FORMAT J = spm_ness_J(P,M,X)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_ness_J.m)
  """

  return _Runtime.call("spm_ness_J", *args, **kwargs)
