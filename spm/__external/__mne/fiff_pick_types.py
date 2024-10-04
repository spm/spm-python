from spm.__wrap__ import _Runtime


def fiff_pick_types(*args, **kwargs):
  """   
    [sel] = fiff_pick_types(info,meg,eeg,stim,exclude)  
     
    Create a selector to pick desired channel types from data  
     
    info      - The measurement info  
    meg       - Include MEG channels  
    eeg       - Include EEG channels  
    stim      - Include stimulus channels  
    include   - Additional channels to include (if empty, do not add any)  
    exclude   - Channels to exclude (if empty, do not exclude any)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_pick_types.m)
  """

  return _Runtime.call("fiff_pick_types", *args, **kwargs)
