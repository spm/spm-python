from spm.__wrap__ import _Runtime


def bf_group(*args, **kwargs):
  """  A module for applying a processing step to a group of subjects  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_group.m)
  """

  return _Runtime.call("bf_group", *args, **kwargs)
