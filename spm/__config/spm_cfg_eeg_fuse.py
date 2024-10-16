from spm.__wrapper__ import Runtime


def spm_cfg_eeg_fuse(*args, **kwargs):
  """  Configuration file for fusing M/EEG files  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_fuse.m)
  """

  return Runtime.call("spm_cfg_eeg_fuse", *args, **kwargs)
