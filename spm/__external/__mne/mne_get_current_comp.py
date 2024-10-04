from spm.__wrap__ import _Runtime


def mne_get_current_comp(*args, **kwargs):
  """   
    [comp] = mne_get_current_comp(info)  
     
    Get the current compensation in effect in the data  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_get_current_comp.m)
  """

  return _Runtime.call("mne_get_current_comp", *args, **kwargs)
