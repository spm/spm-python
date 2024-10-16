from spm.__wrapper__ import Runtime


def spm_cfg_eeg_bc(*args, **kwargs):
  """  configuration file for baseline correction  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_bc.m)
  """

  return Runtime.call("spm_cfg_eeg_bc", *args, **kwargs)
