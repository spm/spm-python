from spm.__wrapper__ import Runtime


def bf_inverse(*args, **kwargs):
  """  Compute inverse projectors  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_inverse.m)
  """

  return Runtime.call("bf_inverse", *args, **kwargs)
