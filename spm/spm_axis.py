from spm.__wrap__ import _Runtime


def spm_axis(*args, **kwargs):
  """  AXIS  Control axis scaling and appearance.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_axis.m)
  """

  return _Runtime.call("spm_axis", *args, **kwargs)
