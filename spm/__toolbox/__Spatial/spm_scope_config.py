from spm.__wrapper__ import Runtime


def spm_scope_config(*args, **kwargs):
  """  SPM Configuration file for SCOPE distortion correction  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Spatial/spm_scope_config.m)
  """

  return Runtime.call("spm_scope_config", *args, **kwargs)
