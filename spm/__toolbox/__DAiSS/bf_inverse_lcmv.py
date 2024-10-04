from spm.__wrap__ import _Runtime


def bf_inverse_lcmv(*args, **kwargs):
  """  Computes LCMV filters  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_inverse_lcmv.m)
  """

  return _Runtime.call("bf_inverse_lcmv", *args, **kwargs)
