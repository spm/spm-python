from spm.__wrap__ import _Runtime


def bf_output_image_mv(*args, **kwargs):
  """  Compute multivariate test on a number of frequency bands  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_output_image_mv.m)
  """

  return _Runtime.call("bf_output_image_mv", *args, **kwargs)
