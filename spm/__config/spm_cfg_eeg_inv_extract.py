from spm.__wrap__ import _Runtime


def spm_cfg_eeg_inv_extract(*args, **kwargs):
  """  Configuration file for extracting source data from imaging source  
    reconstruction  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_inv_extract.m)
  """

  return _Runtime.call("spm_cfg_eeg_inv_extract", *args, **kwargs)
