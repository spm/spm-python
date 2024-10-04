from spm.__wrap__ import _Runtime


def bf_output_image_gain(*args, **kwargs):
  """  Compute gain image  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_output_image_gain.m)
  """

  return _Runtime.call("bf_output_image_gain", *args, **kwargs)
