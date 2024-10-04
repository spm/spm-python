from spm.__wrap__ import _Runtime


def spm_cfg_eeg_collapse_timefreq(*args, **kwargs):
  """  Configuration file for within-image averaging  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_collapse_timefreq.m)
  """

  return _Runtime.call("spm_cfg_eeg_collapse_timefreq", *args, **kwargs)
