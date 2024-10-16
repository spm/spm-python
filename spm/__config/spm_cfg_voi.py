from spm.__wrapper__ import Runtime


def spm_cfg_voi(*args, **kwargs):
  """  SPM Configuration file for VOIs  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_voi.m)
  """

  return Runtime.call("spm_cfg_voi", *args, **kwargs)
