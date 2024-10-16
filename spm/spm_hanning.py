from spm.__wrapper__ import Runtime


def spm_hanning(*args, **kwargs):
  """  Return the n-point Hanning window in a column vector  
    FORMAT H = spm_hanning(n)  
    n  -  length of hanning function  
    H  -  hanning function  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_hanning.m)
  """

  return Runtime.call("spm_hanning", *args, **kwargs)
