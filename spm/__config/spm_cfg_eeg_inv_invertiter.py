from spm.__wrap__ import _Runtime


def spm_cfg_eeg_inv_invertiter(*args, **kwargs):
  """  Configuration file for running imaging source reconstruction  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_inv_invertiter.m)
  """

  return _Runtime.call("spm_cfg_eeg_inv_invertiter", *args, **kwargs)
