from spm.__wrap__ import _Runtime


def spm_cfg_eeg_inv_headmodel(*args, **kwargs):
  """  Configuration file for specifying the head model for source reconstruction  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_inv_headmodel.m)
  """

  return _Runtime.call("spm_cfg_eeg_inv_headmodel", *args, **kwargs)
