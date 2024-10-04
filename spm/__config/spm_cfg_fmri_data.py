from spm.__wrap__ import _Runtime


def spm_cfg_fmri_data(*args, **kwargs):
  """  SPM Configuration file for fMRI data specification  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_fmri_data.m)
  """

  return _Runtime.call("spm_cfg_fmri_data", *args, **kwargs)
