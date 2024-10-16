from spm.__wrapper__ import Runtime


def bf_sources_mni_coords(*args, **kwargs):
  """  Generate beamforming grid  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_sources_mni_coords.m)
  """

  return Runtime.call("bf_sources_mni_coords", *args, **kwargs)
