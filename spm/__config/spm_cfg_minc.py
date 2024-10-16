from spm.__wrapper__ import Runtime


def spm_cfg_minc(*args, **kwargs):
  """  SPM Configuration file for MINC Import  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_minc.m)
  """

  return Runtime.call("spm_cfg_minc", *args, **kwargs)
