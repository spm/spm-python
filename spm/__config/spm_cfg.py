from spm.__wrapper__ import Runtime


def spm_cfg(*args, **kwargs):
  """  SPM Configuration file for MATLABBATCH  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg.m)
  """

  return Runtime.call("spm_cfg", *args, **kwargs)
