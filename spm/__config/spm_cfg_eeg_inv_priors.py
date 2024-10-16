from spm.__wrapper__ import Runtime


def spm_cfg_eeg_inv_priors(*args, **kwargs):
  """  Configuration file to set up priors for M/EEG source reconstruction  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_inv_priors.m)
  """

  return Runtime.call("spm_cfg_eeg_inv_priors", *args, **kwargs)
