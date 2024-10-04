from spm.__wrap__ import _Runtime


def spm_cfg_eeg_contrast(*args, **kwargs):
  """  Configuration file for computing contrast over epochs  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_contrast.m)
  """

  return _Runtime.call("spm_cfg_eeg_contrast", *args, **kwargs)
