from spm.__wrap__ import _Runtime


def spm_cfg_eeg_inv_post(*args, **kwargs):
  """  Configuration file for taking a number of previous inversion results  
    (maybe based on different data), smoothing and creating an approximate posterior  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_inv_post.m)
  """

  return _Runtime.call("spm_cfg_eeg_inv_post", *args, **kwargs)
