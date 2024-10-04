from spm.__wrap__ import _Runtime


def spm_cfg_eeg_review(*args, **kwargs):
  """  Configuration file for M/EEG reviewing tool  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_review.m)
  """

  return _Runtime.call("spm_cfg_eeg_review", *args, **kwargs)
