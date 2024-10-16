from spm.__wrapper__ import Runtime


def spm_cfg_dcm_est(*args, **kwargs):
  """  SPM Configuration file for DCM estimation  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_dcm_est.m)
  """

  return Runtime.call("spm_cfg_dcm_est", *args, **kwargs)
