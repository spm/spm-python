from spm.__wrap__ import _Runtime


def fiff_read_evoked(*args, **kwargs):
  """   
    [data] = fiff_read_evoked(fname,setno)  
     
    Read one evoked data set  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_read_evoked.m)
  """

  return _Runtime.call("fiff_read_evoked", *args, **kwargs)
