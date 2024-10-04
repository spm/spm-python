from spm.__wrap__ import _Runtime


def mne_ex_data_sets(*args, **kwargs):
  """      
      Find all evoked response data from a given file  
     
      [res] = mne_ex_data_sets(fname)  
     
      fname   - Name of the file to look at  
      res     - Structure containing the result  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_ex_data_sets.m)
  """

  return _Runtime.call("mne_ex_data_sets", *args, **kwargs)
