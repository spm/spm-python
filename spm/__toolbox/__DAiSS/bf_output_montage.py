from spm.__wrapper__ import Runtime


def bf_output_montage(*args, **kwargs):
  """  Generate a montage for source extraction  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_output_montage.m)
  """

  return Runtime.call("bf_output_montage", *args, **kwargs)
