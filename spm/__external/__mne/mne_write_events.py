from spm.__wrapper__ import Runtime


def mne_write_events(*args, **kwargs):
  """   
    mne_write_events(filename,eventlist)  
     
    Write an event list into a fif file  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_write_events.m)
  """

  return Runtime.call("mne_write_events", *args, **kwargs, nargout=0)
