from spm.__wrap__ import _Runtime


def spm_cfg_eeg_copy(*args, **kwargs):
  """  Configuration file for copying M/EEG datasets  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_copy.m)
  """

  return _Runtime.call("spm_cfg_eeg_copy", *args, **kwargs)
