from spm.__wrap__ import _Runtime


def spm_eeg_fixpnt(*args, **kwargs):
  """  Helper function to replace pos by pnt  
    FORMAT data = spm_eeg_fixpnt(data, recurse)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_fixpnt.m)
  """

  return _Runtime.call("spm_eeg_fixpnt", *args, **kwargs)
