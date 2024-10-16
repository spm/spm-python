from spm.__wrapper__ import Runtime


def fiff_read_evoked_all(*args, **kwargs):
  """   
    [data] = fiff_read_evoked_all(fname)  
     
    Read all evoked data set (averages only)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_read_evoked_all.m)
  """

  return Runtime.call("fiff_read_evoked_all", *args, **kwargs)
