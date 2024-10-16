from spm.__wrapper__ import Runtime


def fiff_read_epochs(*args, **kwargs):
  """   
    [epochs] = fiff_read_epochs(fname,setno)  
     
    Read epochs from file  
     
     
      Author : Martin Luessi, MGH Martinos Center  
      License : BSD 3-clause  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_read_epochs.m)
  """

  return Runtime.call("fiff_read_epochs", *args, **kwargs)
