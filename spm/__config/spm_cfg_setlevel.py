from spm.__wrap__ import _Runtime


def spm_cfg_setlevel(*args, **kwargs):
  """  SPM Configuration file for Set level tests based on Barnes et al. NIMG  
    2012  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_setlevel.m)
  """

  return _Runtime.call("spm_cfg_setlevel", *args, **kwargs)
