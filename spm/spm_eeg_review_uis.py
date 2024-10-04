from spm.__wrap__ import _Runtime


def spm_eeg_review_uis(*args, **kwargs):
  """  GUI of the M/EEG Review facility  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_review_uis.m)
  """

  return _Runtime.call("spm_eeg_review_uis", *args, **kwargs)
