from spm.__wrap__ import _Runtime


def spm_cfg_disp(*args, **kwargs):
  """  SPM Configuration file for Image Display  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_disp.m)
  """

  return _Runtime.call("spm_cfg_disp", *args, **kwargs)
