from spm.__wrap__ import _Runtime


def spm_sum(*args, **kwargs):
  """  Sum of elements  
    FORMAT S = spm_sum(X,vecdim)  
     
    Compatibility layer for SUM for MATLAB < R2018b  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_sum.m)
  """

  return _Runtime.call("spm_sum", *args, **kwargs)
