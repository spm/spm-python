from spm.__wrap__ import _Runtime


def bf_sources_voi(*args, **kwargs):
  """  Generate a set of VOIs specified in MNI coordinates  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_sources_voi.m)
  """

  return _Runtime.call("bf_sources_voi", *args, **kwargs)
