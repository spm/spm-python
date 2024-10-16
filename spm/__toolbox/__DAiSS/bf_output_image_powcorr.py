from spm.__wrapper__ import Runtime


def bf_output_image_powcorr(*args, **kwargs):
  """  Compute phase-amplitude coupling  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_output_image_powcorr.m)
  """

  return Runtime.call("bf_output_image_powcorr", *args, **kwargs)
