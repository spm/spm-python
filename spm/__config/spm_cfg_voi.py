from spm.__wrap__ import _Runtime


def spm_cfg_voi(*args, **kwargs):
  """  SPM Configuration file for VOIs  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_voi.m)
  """

  return _Runtime.call("spm_cfg_voi", *args, **kwargs)
