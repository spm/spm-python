from spm.__wrapper__ import Runtime


def spm_eeg_review_switchDisplay(*args, **kwargs):
  """  Switch between displays in the M/EEG Review facility  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_review_switchDisplay.m)
  """

  return Runtime.call("spm_eeg_review_switchDisplay", *args, **kwargs)
