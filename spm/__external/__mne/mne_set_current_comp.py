from spm.__wrap__ import _Runtime


def mne_set_current_comp(*args, **kwargs):
  """   
    mne_set_current_comp(chs,value)  
     
    Set the current compensation value in the channel info structures  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_set_current_comp.m)
  """

  return _Runtime.call("mne_set_current_comp", *args, **kwargs)
