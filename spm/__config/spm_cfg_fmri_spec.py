from spm.__wrap__ import _Runtime


def spm_cfg_fmri_spec(*args, **kwargs):
  """  SPM Configuration file for fMRI model specification  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_fmri_spec.m)
  """

  return _Runtime.call("spm_cfg_fmri_spec", *args, **kwargs)
