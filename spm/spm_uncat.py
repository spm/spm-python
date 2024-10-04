from spm.__wrap__ import _Runtime


def spm_uncat(*args, **kwargs):
  """  Convert a matrix into an array  
    FORMAT [a] = spm_uncat(x,a)  
    x - matrix  
    a - cell array  
     
    i.e. a = spm_uncat(spm_cat(a),a)  
     
    see also spm_vec and spm_unvec  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_uncat.m)
  """

  return _Runtime.call("spm_uncat", *args, **kwargs)
