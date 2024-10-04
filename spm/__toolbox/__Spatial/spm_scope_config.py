from spm.__wrap__ import _Runtime


def spm_scope_config(*args, **kwargs):
  """  SPM Configuration file for SCOPE distortion correction  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Spatial/spm_scope_config.m)
  """

  return _Runtime.call("spm_scope_config", *args, **kwargs)
