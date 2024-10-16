from spm.__wrapper__ import Runtime


def mne_read_inverse_operator(*args, **kwargs):
  """   
    [inv] = mne_read_inverse_operator(fname)  
     
    Reads the inverse operator decomposition from a fif file  
     
    fname        - The name of the file  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_read_inverse_operator.m)
  """

  return Runtime.call("mne_read_inverse_operator", *args, **kwargs)
