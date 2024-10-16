from spm.__wrapper__ import Runtime


def bf_regularise_mantrunc(*args, **kwargs):
  """  User-specified dimensional reduction  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_regularise_mantrunc.m)
  """

  return Runtime.call("bf_regularise_mantrunc", *args, **kwargs)
