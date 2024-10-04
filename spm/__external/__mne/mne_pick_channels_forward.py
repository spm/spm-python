from spm.__wrap__ import _Runtime


def mne_pick_channels_forward(*args, **kwargs):
  """   
    [fwd] = mne_pick_channels_forward(orig,include,exclude)  
     
    Pick desired channels from a forward solution  
     
    orig      - The original forward solution  
    include   - Channels to include (if empty, include all available)  
    exclude   - Channels to exclude (if empty, do not exclude any)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_pick_channels_forward.m)
  """

  return _Runtime.call("mne_pick_channels_forward", *args, **kwargs)
