from spm.__wrapper__ import Runtime


def spm_cfg_factorial_design(*args, **kwargs):
  """  SPM Configuration file for second-level models  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_factorial_design.m)
  """

  return Runtime.call("spm_cfg_factorial_design", *args, **kwargs)
