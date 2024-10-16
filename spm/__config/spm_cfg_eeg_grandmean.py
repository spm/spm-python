from spm.__wrapper__ import Runtime


def spm_cfg_eeg_grandmean(*args, **kwargs):
  """  Configuration file for averaging evoked responses  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_grandmean.m)
  """

  return Runtime.call("spm_cfg_eeg_grandmean", *args, **kwargs)
