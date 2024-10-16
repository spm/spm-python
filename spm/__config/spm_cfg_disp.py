from spm.__wrapper__ import Runtime


def spm_cfg_disp(*args, **kwargs):
  """  SPM Configuration file for Image Display  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_disp.m)
  """

  return Runtime.call("spm_cfg_disp", *args, **kwargs)
