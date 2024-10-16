from spm.__wrapper__ import Runtime


def spm_cfg_eeg_inv_simulate(*args, **kwargs):
  """  Configuration file for simulation of sources  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_inv_simulate.m)
  """

  return Runtime.call("spm_cfg_eeg_inv_simulate", *args, **kwargs)
