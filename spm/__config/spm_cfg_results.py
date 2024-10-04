from spm.__wrap__ import _Runtime


def spm_cfg_results(*args, **kwargs):
  """  SPM Configuration file for Results Report  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_results.m)
  """

  return _Runtime.call("spm_cfg_results", *args, **kwargs)
