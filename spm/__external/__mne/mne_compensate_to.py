from spm.__wrapper__ import Runtime


def mne_compensate_to(*args, **kwargs):
  """   
    [newdata] = mne_compensate_to(data,to)  
     
    Apply compensation to the data as desired  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_compensate_to.m)
  """

  return Runtime.call("mne_compensate_to", *args, **kwargs)
