from spm.__wrapper__ import Runtime


def spm_cfg_results(*args, **kwargs):
  """  SPM Configuration file for Results Report  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_results.m)
  """

  return Runtime.call("spm_cfg_results", *args, **kwargs)
