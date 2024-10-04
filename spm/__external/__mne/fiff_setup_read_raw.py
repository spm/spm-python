from spm.__wrap__ import _Runtime


def fiff_setup_read_raw(*args, **kwargs):
  """   
    [data] = fiff_setup_read_raw(fname,allow_maxshield)  
     
    Read information about raw data file  
     
    fname               Name of the file to read  
    allow_maxshield     Accept unprocessed MaxShield data  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_setup_read_raw.m)
  """

  return _Runtime.call("fiff_setup_read_raw", *args, **kwargs)
