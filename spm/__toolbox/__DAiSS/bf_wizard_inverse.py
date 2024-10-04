from spm.__wrap__ import _Runtime


def bf_wizard_inverse(*args, **kwargs):
  """  A handy command-line based batch filler with some defaults for DAiSS  
    invert module, pick a few options, and it will default for unpopulated  
    fields  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_wizard_inverse.m)
  """

  return _Runtime.call("bf_wizard_inverse", *args, **kwargs)
