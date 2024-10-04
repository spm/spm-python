from spm.__wrap__ import _Runtime


def spm_cfg_eeg_inv_optimize(*args, **kwargs):
  """  Configuration file to set up optimization routines for M/EEG source  
    inversion  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_inv_optimize.m)
  """

  return _Runtime.call("spm_cfg_eeg_inv_optimize", *args, **kwargs)
