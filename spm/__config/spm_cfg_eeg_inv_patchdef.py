from spm.__wrapper__ import Runtime


def spm_cfg_eeg_inv_patchdef(*args, **kwargs):
  """  Configuration file for taking a number of previous inversion results  
    (maybe based on different data), smoothing and creating an approximate posterior  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_inv_patchdef.m)
  """

  return Runtime.call("spm_cfg_eeg_inv_patchdef", *args, **kwargs)
