from spm.__wrap__ import _Runtime


def fiff_reset_ch_pos(*args, **kwargs):
  """   
    [res] = fiff_reset_ch_pos(chs)  
     
    Reset channel position data to their original values as listed in  
    the fif file  
     
    NOTE: Only the coil_trans field is modified by this routine, not  
    loc which remains to reflect the original data read from the fif file  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_reset_ch_pos.m)
  """

  return _Runtime.call("fiff_reset_ch_pos", *args, **kwargs)
