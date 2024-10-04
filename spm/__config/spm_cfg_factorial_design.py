from spm.__wrap__ import _Runtime


def spm_cfg_factorial_design(*args, **kwargs):
  """  SPM Configuration file for second-level models  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_factorial_design.m)
  """

  return _Runtime.call("spm_cfg_factorial_design", *args, **kwargs)
