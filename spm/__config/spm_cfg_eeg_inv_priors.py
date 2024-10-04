from spm.__wrap__ import _Runtime


def spm_cfg_eeg_inv_priors(*args, **kwargs):
  """  Configuration file to set up priors for M/EEG source reconstruction  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_inv_priors.m)
  """

  return _Runtime.call("spm_cfg_eeg_inv_priors", *args, **kwargs)
