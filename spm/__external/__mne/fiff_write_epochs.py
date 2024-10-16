from spm.__wrapper__ import Runtime


def fiff_write_epochs(*args, **kwargs):
  """   
    function fiff_write_epochs(name,data)  
     
    name     filename  
    data     the data structure returned from fiff_write_evoked  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_write_epochs.m)
  """

  return Runtime.call("fiff_write_epochs", *args, **kwargs, nargout=0)
