from spm.__wrap__ import _Runtime


def fiff_pick_channels_evoked(*args, **kwargs):
  """   
    [res] = fiff_pick_channels_evoked(orig,include,exclude)  
     
    Pick desired channels from evoked-response data  
     
    orig      - The original data  
    include   - Channels to include (if empty, include all available)  
    exclude   - Channels to exclude (if empty, do not exclude any)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_pick_channels_evoked.m)
  """

  return _Runtime.call("fiff_pick_channels_evoked", *args, **kwargs)
