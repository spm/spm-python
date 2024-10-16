from spm.__wrapper__ import Runtime


def spm_MB_col(*args, **kwargs):
  """  Return colours and marker size for number of partitions  
    FORMAT [col,bol,msz] = spm_MB_col(n)  
    n  - number of partitions  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_MB_col.m)
  """

  return Runtime.call("spm_MB_col", *args, **kwargs)
