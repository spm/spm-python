from spm.__wrapper__ import Runtime


def bf_std_fields(*args, **kwargs):
  """   
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_std_fields.m)
  """

  return Runtime.call("bf_std_fields", *args, **kwargs)
