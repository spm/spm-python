from spm.__wrapper__ import Runtime


def bf_load(*args, **kwargs):
  """  Load BF data into memory with just the requested fields  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_load.m)
  """

  return Runtime.call("bf_load", *args, **kwargs)
