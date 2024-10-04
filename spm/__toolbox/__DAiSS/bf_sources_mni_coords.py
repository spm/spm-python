from spm.__wrap__ import _Runtime


def bf_sources_mni_coords(*args, **kwargs):
  """  Generate beamforming grid  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_sources_mni_coords.m)
  """

  return _Runtime.call("bf_sources_mni_coords", *args, **kwargs)
