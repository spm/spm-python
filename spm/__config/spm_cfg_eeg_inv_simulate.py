from spm.__wrap__ import _Runtime


def spm_cfg_eeg_inv_simulate(*args, **kwargs):
  """  Configuration file for simulation of sources  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_inv_simulate.m)
  """

  return _Runtime.call("spm_cfg_eeg_inv_simulate", *args, **kwargs)
