from spm.__wrap__ import _Runtime


def spm_cfg_eeg_crop(*args, **kwargs):
  """  configuration file for cropping M/EEG data  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_crop.m)
  """

  return _Runtime.call("spm_cfg_eeg_crop", *args, **kwargs)
