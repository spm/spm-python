from spm.__wrapper__ import Runtime


def spm_cfg_reorient(*args, **kwargs):
  """  SPM Configuration file for Reorient Images  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_reorient.m)
  """

  return Runtime.call("spm_cfg_reorient", *args, **kwargs)
