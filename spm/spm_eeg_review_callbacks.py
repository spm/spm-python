from spm.__wrapper__ import Runtime


def spm_eeg_review_callbacks(*args, **kwargs):
  """  Callbacks of the M/EEG Review facility  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_review_callbacks.m)
  """

  return Runtime.call("spm_eeg_review_callbacks", *args, **kwargs)
