from spm.__wrapper__ import Runtime


def spm_cfg_eeg_channel_selector(*args, **kwargs):
  """  Generic M/EEG channel selector based on label and type  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_channel_selector.m)
  """

  return Runtime.call("spm_cfg_eeg_channel_selector", *args, **kwargs)
