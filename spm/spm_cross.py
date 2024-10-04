from spm.__wrap__ import _Runtime


def spm_cross(*args, **kwargs):
  """  Multidimensional cross (outer) product  
    FORMAT [Y] = spm_cross(X,x)  
    FORMAT [Y] = spm_cross(X)  
     
    X  - numeric array  
    x  - numeric array  
     
    Y  - outer product  
     
    See also: spm_dot  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_cross.m)
  """

  return _Runtime.call("spm_cross", *args, **kwargs)
