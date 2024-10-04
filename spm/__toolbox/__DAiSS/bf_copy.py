from spm.__wrap__ import _Runtime


def bf_copy(*args, **kwargs):
  """  Set up a new analysis by copying an existing one  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_copy.m)
  """

  return _Runtime.call("bf_copy", *args, **kwargs)
