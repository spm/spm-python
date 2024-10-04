from spm.__wrap__ import _Runtime


def spm_cfg_deface(*args, **kwargs):
  """  SPM Configuration file for toolbox 'De-Face'  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_deface.m)
  """

  return _Runtime.call("spm_cfg_deface", *args, **kwargs)
