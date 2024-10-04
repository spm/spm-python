from spm.__wrap__ import _Runtime


def spm_cfg_fmri_est(*args, **kwargs):
  """  SPM Configuration file for Model Estimation  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_fmri_est.m)
  """

  return _Runtime.call("spm_cfg_fmri_est", *args, **kwargs)
