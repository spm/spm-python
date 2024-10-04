from spm.__wrap__ import _Runtime


def spm_hanning(*args, **kwargs):
  """  Return the n-point Hanning window in a column vector  
    FORMAT H = spm_hanning(n)  
    n  -  length of hanning function  
    H  -  hanning function  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_hanning.m)
  """

  return _Runtime.call("spm_hanning", *args, **kwargs)
