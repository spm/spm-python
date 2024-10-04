from spm.__wrap__ import _Runtime


def spm_cfg_dcm_bms(*args, **kwargs):
  """  Configuration file for Bayesian Model Selection (DCM)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_dcm_bms.m)
  """

  return _Runtime.call("spm_cfg_dcm_bms", *args, **kwargs)
