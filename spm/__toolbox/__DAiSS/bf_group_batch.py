from spm.__wrapper__ import Runtime


def bf_group_batch(*args, **kwargs):
  """  Run a DAiSS batch on a group of subjects  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_group_batch.m)
  """

  return Runtime.call("bf_group_batch", *args, **kwargs)
