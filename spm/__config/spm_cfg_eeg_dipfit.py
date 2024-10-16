from spm.__wrapper__ import Runtime


def spm_cfg_eeg_dipfit(*args, **kwargs):
  """  Configuration file for Bayesian dipole fitting  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_dipfit.m)
  """

  return Runtime.call("spm_cfg_eeg_dipfit", *args, **kwargs)
