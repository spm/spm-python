from spm.__wrap__ import _Runtime


def spm_eeg_review_callbacks(*args, **kwargs):
  """  Callbacks of the M/EEG Review facility  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_review_callbacks.m)
  """

  return _Runtime.call("spm_eeg_review_callbacks", *args, **kwargs)
