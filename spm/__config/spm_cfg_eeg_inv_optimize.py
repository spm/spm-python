from spm.__wrapper__ import Runtime


def spm_cfg_eeg_inv_optimize(*args, **kwargs):
  """  Configuration file to set up optimization routines for M/EEG source  
    inversion  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_inv_optimize.m)
  """

  return Runtime.call("spm_cfg_eeg_inv_optimize", *args, **kwargs)
