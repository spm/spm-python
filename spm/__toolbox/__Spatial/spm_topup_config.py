from spm.__wrapper__ import Runtime


def spm_topup_config(*args, **kwargs):
  """  SPM Configuration file for Topup  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Spatial/spm_topup_config.m)
  """

  return Runtime.call("spm_topup_config", *args, **kwargs)
