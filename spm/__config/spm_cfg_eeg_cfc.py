from spm.__wrap__ import _Runtime


def spm_cfg_eeg_cfc(*args, **kwargs):
  """  Configuration file for M/EEG cross-frequency coupling analysis  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_cfc.m)
  """

  return _Runtime.call("spm_cfg_eeg_cfc", *args, **kwargs)
