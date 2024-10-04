from spm.__wrap__ import _Runtime


def spm_log(*args, **kwargs):
  """  Log of numeric array plus a small constant  
    FORMAT A = spm_log(A)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_log.m)
  """

  return _Runtime.call("spm_log", *args, **kwargs)
