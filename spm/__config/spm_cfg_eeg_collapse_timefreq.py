from spm.__wrapper__ import Runtime


def spm_cfg_eeg_collapse_timefreq(*args, **kwargs):
  """  Configuration file for within-image averaging  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_collapse_timefreq.m)
  """

  return Runtime.call("spm_cfg_eeg_collapse_timefreq", *args, **kwargs)
