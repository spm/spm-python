from spm.__wrap__ import _Runtime


def fiff_pick_channels(*args, **kwargs):
  """   
    [sel] = fiff_pick_channels(ch_names,include,exclude)  
     
    Make a selector to pick desired channels from data  
     
    ch_names  - The channel name list to consult  
    include   - Channels to include (if empty, include all available)  
    exclude   - Channels to exclude (if empty, do not exclude any)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_pick_channels.m)
  """

  return _Runtime.call("fiff_pick_channels", *args, **kwargs)
