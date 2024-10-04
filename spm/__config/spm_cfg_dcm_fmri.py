from spm.__wrap__ import _Runtime


def spm_cfg_dcm_fmri(*args, **kwargs):
  """  SPM Configuration file for DCM for fMRI  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_dcm_fmri.m)
  """

  return _Runtime.call("spm_cfg_dcm_fmri", *args, **kwargs)
