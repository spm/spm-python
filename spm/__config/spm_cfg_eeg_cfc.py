from spm.__wrapper__ import Runtime


def spm_cfg_eeg_cfc(*args, **kwargs):
  """  Configuration file for M/EEG cross-frequency coupling analysis  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_cfc.m)
  """

  return Runtime.call("spm_cfg_eeg_cfc", *args, **kwargs)
