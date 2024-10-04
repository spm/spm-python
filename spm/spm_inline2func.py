from spm.__wrap__ import _Runtime


def spm_inline2func(*args, **kwargs):
  """  Convert an inline object to a function handle  
    FORMAT [h] = spm_inline2func(f)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_inline2func.m)
  """

  return _Runtime.call("spm_inline2func", *args, **kwargs)
