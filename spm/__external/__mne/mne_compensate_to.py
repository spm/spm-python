from spm.__wrap__ import _Runtime


def mne_compensate_to(*args, **kwargs):
  """   
    [newdata] = mne_compensate_to(data,to)  
     
    Apply compensation to the data as desired  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_compensate_to.m)
  """

  return _Runtime.call("mne_compensate_to", *args, **kwargs)
