from spm.__wrapper__ import Runtime


def spm_cfg_eeg_prepare(*args, **kwargs):
  """  Configuration file for the prepare tool  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_prepare.m)
  """

  return Runtime.call("spm_cfg_eeg_prepare", *args, **kwargs)
