from spm.__wrap__ import _Runtime


def spm_zeros(*args, **kwargs):
  """  Fill a cell or structure array with zeros  
    FORMAT [X] = spm_zeros(X)  
    X  - numeric, cell or structure array[s]  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_zeros.m)
  """

  return _Runtime.call("spm_zeros", *args, **kwargs)
