from spm.__wrapper__ import Runtime


def spm_cfg_eeg_merge(*args, **kwargs):
  """  Configuration file for merging M/EEG files  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_merge.m)
  """

  return Runtime.call("spm_cfg_eeg_merge", *args, **kwargs)
