from spm.__wrap__ import _Runtime


def bf_inverse(*args, **kwargs):
  """  Compute inverse projectors  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_inverse.m)
  """

  return _Runtime.call("bf_inverse", *args, **kwargs)
