from spm.__wrap__ import _Runtime


def bf_sources_grid_phantom(*args, **kwargs):
  """  Generate beamforming grid  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_sources_grid_phantom.m)
  """

  return _Runtime.call("bf_sources_grid_phantom", *args, **kwargs)
