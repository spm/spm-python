from spm.__wrapper__ import Runtime


def spm_cfg_checkreg(*args, **kwargs):
  """  SPM Configuration file for Check Reg  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_checkreg.m)
  """

  return Runtime.call("spm_cfg_checkreg", *args, **kwargs)
