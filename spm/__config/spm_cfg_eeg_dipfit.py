from spm.__wrap__ import _Runtime


def spm_cfg_eeg_dipfit(*args, **kwargs):
  """  Configuration file for Bayesian dipole fitting  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_dipfit.m)
  """

  return _Runtime.call("spm_cfg_eeg_dipfit", *args, **kwargs)
