from spm.__wrapper__ import Runtime


def spm_squeeze(*args, **kwargs):
  """  Version of squeeze with the possibility to select the dimensions to remove  
    FORMAT  B = spm_squeeze(A, dim)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_squeeze.m)
  """

  return Runtime.call("spm_squeeze", *args, **kwargs)
