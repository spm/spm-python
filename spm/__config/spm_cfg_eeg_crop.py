from spm.__wrapper__ import Runtime


def spm_cfg_eeg_crop(*args, **kwargs):
  """  configuration file for cropping M/EEG data  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_crop.m)
  """

  return Runtime.call("spm_cfg_eeg_crop", *args, **kwargs)
