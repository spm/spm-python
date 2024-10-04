from spm.__wrap__ import _Runtime


def spm_cfg_eeg_channel_selector(*args, **kwargs):
  """  Generic M/EEG channel selector based on label and type  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_channel_selector.m)
  """

  return _Runtime.call("spm_cfg_eeg_channel_selector", *args, **kwargs)
