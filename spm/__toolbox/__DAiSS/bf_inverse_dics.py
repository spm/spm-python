from spm.__wrap__ import _Runtime


def bf_inverse_dics(*args, **kwargs):
  """  Computes DICS filters  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_inverse_dics.m)
  """

  return _Runtime.call("bf_inverse_dics", *args, **kwargs)
