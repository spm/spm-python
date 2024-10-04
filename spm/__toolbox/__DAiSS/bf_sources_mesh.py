from spm.__wrap__ import _Runtime


def bf_sources_mesh(*args, **kwargs):
  """  Generate cortical mesh  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_sources_mesh.m)
  """

  return _Runtime.call("bf_sources_mesh", *args, **kwargs)
