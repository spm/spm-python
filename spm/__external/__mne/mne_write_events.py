from spm.__wrap__ import _Runtime


def mne_write_events(*args, **kwargs):
  """   
    mne_write_events(filename,eventlist)  
     
    Write an event list into a fif file  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_write_events.m)
  """

  return _Runtime.call("mne_write_events", *args, **kwargs, nargout=0)
