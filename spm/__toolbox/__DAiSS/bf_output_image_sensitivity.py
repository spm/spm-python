from spm.__wrap__ import _Runtime


def bf_output_image_sensitivity(*args, **kwargs):
  """  Sensitivity profile for a group of sensors  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_output_image_sensitivity.m)
  """

  return _Runtime.call("bf_output_image_sensitivity", *args, **kwargs)
