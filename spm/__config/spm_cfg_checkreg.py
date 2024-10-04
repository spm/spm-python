from spm.__wrap__ import _Runtime


def spm_cfg_checkreg(*args, **kwargs):
  """  SPM Configuration file for Check Reg  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_checkreg.m)
  """

  return _Runtime.call("spm_cfg_checkreg", *args, **kwargs)
