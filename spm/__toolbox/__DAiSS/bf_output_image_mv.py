from spm.__wrapper__ import Runtime


def bf_output_image_mv(*args, **kwargs):
  """  Compute multivariate test on a number of frequency bands  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_output_image_mv.m)
  """

  return Runtime.call("bf_output_image_mv", *args, **kwargs)
