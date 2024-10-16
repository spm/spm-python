from spm.__wrapper__ import Runtime


def bf_sources_voi(*args, **kwargs):
  """  Generate a set of VOIs specified in MNI coordinates  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_sources_voi.m)
  """

  return Runtime.call("bf_sources_voi", *args, **kwargs)
