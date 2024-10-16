from spm.__wrapper__ import Runtime


def spm_axis(*args, **kwargs):
  """  AXIS  Control axis scaling and appearance.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_axis.m)
  """

  return Runtime.call("spm_axis", *args, **kwargs)
