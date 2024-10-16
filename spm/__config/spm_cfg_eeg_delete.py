from spm.__wrapper__ import Runtime


def spm_cfg_eeg_delete(*args, **kwargs):
  """  Configuration file for deleting M/EEG datasets  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_delete.m)
  """

  return Runtime.call("spm_cfg_eeg_delete", *args, **kwargs)
