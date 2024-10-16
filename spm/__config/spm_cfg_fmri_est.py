from spm.__wrapper__ import Runtime


def spm_cfg_fmri_est(*args, **kwargs):
  """  SPM Configuration file for Model Estimation  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_fmri_est.m)
  """

  return Runtime.call("spm_cfg_fmri_est", *args, **kwargs)
