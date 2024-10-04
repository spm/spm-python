from spm.__wrap__ import _Runtime


def bf_regularise_mantrunc(*args, **kwargs):
  """  User-specified dimensional reduction  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_regularise_mantrunc.m)
  """

  return _Runtime.call("bf_regularise_mantrunc", *args, **kwargs)
