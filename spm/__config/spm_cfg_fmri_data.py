from spm.__wrapper__ import Runtime


def spm_cfg_fmri_data(*args, **kwargs):
  """  SPM Configuration file for fMRI data specification  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_fmri_data.m)
  """

  return Runtime.call("spm_cfg_fmri_data", *args, **kwargs)
