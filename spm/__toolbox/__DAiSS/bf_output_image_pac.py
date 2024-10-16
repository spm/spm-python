from spm.__wrapper__ import Runtime


def bf_output_image_pac(*args, **kwargs):
  """  Computes phase-amplitude coupling  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_output_image_pac.m)
  """

  return Runtime.call("bf_output_image_pac", *args, **kwargs)
