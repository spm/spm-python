from spm.__wrapper__ import Runtime


def spm_cfg_eeg_avgfreq(*args, **kwargs):
  """  Configuration file for averaging over frequency  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_avgfreq.m)
  """

  return Runtime.call("spm_cfg_eeg_avgfreq", *args, **kwargs)
