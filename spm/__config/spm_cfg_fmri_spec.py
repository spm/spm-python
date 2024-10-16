from spm.__wrapper__ import Runtime


def spm_cfg_fmri_spec(*args, **kwargs):
  """  SPM Configuration file for fMRI model specification  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_fmri_spec.m)
  """

  return Runtime.call("spm_cfg_fmri_spec", *args, **kwargs)
