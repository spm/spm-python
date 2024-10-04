from spm.__wrap__ import _Runtime


def mne_read_inverse_operator(*args, **kwargs):
  """   
    [inv] = mne_read_inverse_operator(fname)  
     
    Reads the inverse operator decomposition from a fif file  
     
    fname        - The name of the file  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_read_inverse_operator.m)
  """

  return _Runtime.call("mne_read_inverse_operator", *args, **kwargs)
