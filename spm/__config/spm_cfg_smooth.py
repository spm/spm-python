from spm.__wrapper__ import Runtime


def spm_cfg_smooth(*args, **kwargs):
  """  SPM Configuration file for Smooth  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_smooth.m)
  """

  return Runtime.call("spm_cfg_smooth", *args, **kwargs)
