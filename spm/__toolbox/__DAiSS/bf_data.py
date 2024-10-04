from spm.__wrap__ import _Runtime


def bf_data(*args, **kwargs):
  """  Prepare the data and initialise the beamforming pipeline  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_data.m)
  """

  return _Runtime.call("bf_data", *args, **kwargs)
