from spm.__wrap__ import _Runtime


def bf_sources(*args, **kwargs):
  """  Prepare source locations and lead fields for beamforming  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_sources.m)
  """

  return _Runtime.call("bf_sources", *args, **kwargs)
