from spm.__wrapper__ import Runtime


def spm_cfg_eeg_filter(*args, **kwargs):
  """  configuration file for EEG filtering  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_filter.m)
  """

  return Runtime.call("spm_cfg_eeg_filter", *args, **kwargs)
