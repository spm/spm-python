from spm.__wrapper__ import Runtime


def _macro_method(*args, **kwargs):
  """  MACRO_METHOD: Script to insert at the beginning of all the brainstorm class functions  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MEEGtools/private/macro_method.m)
  """

  return Runtime.call("macro_method", *args, **kwargs)
