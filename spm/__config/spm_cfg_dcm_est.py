from spm.__wrap__ import _Runtime


def spm_cfg_dcm_est(*args, **kwargs):
  """  SPM Configuration file for DCM estimation  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_dcm_est.m)
  """

  return _Runtime.call("spm_cfg_dcm_est", *args, **kwargs)
