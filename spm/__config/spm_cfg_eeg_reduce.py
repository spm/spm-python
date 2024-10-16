from spm.__wrapper__ import Runtime


def spm_cfg_eeg_reduce(*args, **kwargs):
  """  Configuration file for M/EEG data reduction  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_reduce.m)
  """

  return Runtime.call("spm_cfg_eeg_reduce", *args, **kwargs)
