from spm.__wrap__ import _Runtime


def spm_cfg(*args, **kwargs):
  """  SPM Configuration file for MATLABBATCH  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg.m)
  """

  return _Runtime.call("spm_cfg", *args, **kwargs)
