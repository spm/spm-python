from spm.__wrap__ import _Runtime


def bf_output_image_kurtosis(*args, **kwargs):
  """  Compute kurtosis image  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_output_image_kurtosis.m)
  """

  return _Runtime.call("bf_output_image_kurtosis", *args, **kwargs)
