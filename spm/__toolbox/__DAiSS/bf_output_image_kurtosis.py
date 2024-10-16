from spm.__wrapper__ import Runtime


def bf_output_image_kurtosis(*args, **kwargs):
  """  Compute kurtosis image  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_output_image_kurtosis.m)
  """

  return Runtime.call("bf_output_image_kurtosis", *args, **kwargs)
