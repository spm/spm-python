from spm.__wrapper__ import Runtime


def mne_read_events(*args, **kwargs):
  """   
    [eventlist] = mne_read_events(filename)  
     
    Read an event list from a fif file  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_read_events.m)
  """

  return Runtime.call("mne_read_events", *args, **kwargs)
