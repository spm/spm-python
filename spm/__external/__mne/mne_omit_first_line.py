from spm.__wrap__ import _Runtime


def mne_omit_first_line(*args, **kwargs):
  """   
    [rest] = mne_omit_first_line(str)  
     
    Omit the first line in a multi-line string (useful for handling  
    error messages)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_omit_first_line.m)
  """

  return _Runtime.call("mne_omit_first_line", *args, **kwargs)
