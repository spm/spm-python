from spm.__wrap__ import _Runtime


def spm_MB_col(*args, **kwargs):
  """  Return colours and marker size for number of partitions  
    FORMAT [col,bol,msz] = spm_MB_col(n)  
    n  - number of partitions  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_MB_col.m)
  """

  return _Runtime.call("spm_MB_col", *args, **kwargs)
