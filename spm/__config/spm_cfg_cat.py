from spm.__wrapper__ import Runtime


def spm_cfg_cat(*args, **kwargs):
  """  SPM Configuration file for 3D to 4D volumes conversion  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_cat.m)
  """

  return Runtime.call("spm_cfg_cat", *args, **kwargs)
