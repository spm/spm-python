from spm.__wrapper__ import Runtime


def bf_copy(*args, **kwargs):
  """  Set up a new analysis by copying an existing one  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_copy.m)
  """

  return Runtime.call("bf_copy", *args, **kwargs)
