from spm.__wrap__ import _Runtime


def bf_output_image_dics(*args, **kwargs):
  """  Computes DICS image  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_output_image_dics.m)
  """

  return _Runtime.call("bf_output_image_dics", *args, **kwargs)
