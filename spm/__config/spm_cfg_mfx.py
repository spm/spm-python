from spm.__wrap__ import _Runtime


def spm_cfg_mfx(*args, **kwargs):
  """  SPM Configuration file for MFX  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_mfx.m)
  """

  return _Runtime.call("spm_cfg_mfx", *args, **kwargs)
