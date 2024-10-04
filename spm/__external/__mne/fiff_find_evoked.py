from spm.__wrap__ import _Runtime


def fiff_find_evoked(*args, **kwargs):
  """   
    [data_sets] = fiff_find_evoked(fname)  
     
    Find all evoked data sets in a fif file and create a list of descriptors  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_find_evoked.m)
  """

  return _Runtime.call("fiff_find_evoked", *args, **kwargs)
