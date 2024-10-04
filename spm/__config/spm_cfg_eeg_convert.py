from spm.__wrap__ import _Runtime


def spm_cfg_eeg_convert(*args, **kwargs):
  """  Configuration file for M/EEG data conversion  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_convert.m)
  """

  return _Runtime.call("spm_cfg_eeg_convert", *args, **kwargs)
