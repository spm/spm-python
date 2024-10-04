from spm.__wrap__ import _Runtime


def spm_cfg_dcm_peb(*args, **kwargs):
  """  SPM Configuration file for second-level DCM (PEB)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_dcm_peb.m)
  """

  return _Runtime.call("spm_cfg_dcm_peb", *args, **kwargs)
