from spm.__wrap__ import _Runtime


def spm_vec(*args, **kwargs):
  """  Vectorise a numeric, cell or structure array - a compiled routine  
    FORMAT [vX] = spm_vec(X)  
    X  - numeric, cell or structure array[s]  
    vX - vec(X)  
     
    See spm_unvec  
   __________________________________________________________________________  
     
    e.g.:  
    spm_vec({eye(2) 3}) = [1 0 0 1 3]'  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_vec.m)
  """

  return _Runtime.call("spm_vec", *args, **kwargs)
