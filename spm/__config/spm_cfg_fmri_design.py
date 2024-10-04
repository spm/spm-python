from spm.__wrap__ import _Runtime


def spm_cfg_fmri_design(*args, **kwargs):
  """  SPM Configuration file for fMRI model specification (design only)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_fmri_design.m)
  """

  return _Runtime.call("spm_cfg_fmri_design", *args, **kwargs)
