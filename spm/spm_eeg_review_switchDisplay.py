from spm.__wrap__ import _Runtime


def spm_eeg_review_switchDisplay(*args, **kwargs):
  """  Switch between displays in the M/EEG Review facility  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_review_switchDisplay.m)
  """

  return _Runtime.call("spm_eeg_review_switchDisplay", *args, **kwargs)
