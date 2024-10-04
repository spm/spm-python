from spm.__wrap__ import _Runtime


def fiff_transform_eeg_chs(*args, **kwargs):
  """   
    [res, count] = fiff_transform_eeg_chs(chs,trans)  
     
    Move to another coordinate system in EEG channel channel info  
    Count gives the number of channels transformed  
     
    NOTE: Only the eeg_loc field is modified by this routine, not  
    loc which remains to reflect the original data read from the fif file  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_transform_eeg_chs.m)
  """

  return _Runtime.call("fiff_transform_eeg_chs", *args, **kwargs)
