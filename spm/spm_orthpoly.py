from spm.__wrapper__ import Runtime


def spm_orthpoly(*args, **kwargs):
  """  Create orthonormal polynomial basis functions  
    FORMAT C = spm_orthpoly(N,[K])  
    N - dimension  
    K - order  
   __________________________________________________________________________  
     
    spm_orthpoly creates a matrix for the first few basis functions of an  
    orthogonal polynomial expansion.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_orthpoly.m)
  """

  return Runtime.call("spm_orthpoly", *args, **kwargs)
