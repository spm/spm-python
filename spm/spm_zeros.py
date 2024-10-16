from spm.__wrapper__ import Runtime


def spm_zeros(*args, **kwargs):
  """  Fill a cell or structure array with zeros  
    FORMAT [X] = spm_zeros(X)  
    X  - numeric, cell or structure array[s]  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_zeros.m)
  """

  return Runtime.call("spm_zeros", *args, **kwargs)
