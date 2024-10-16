from spm.__wrapper__ import Runtime


def fiff_write_evoked(*args, **kwargs):
  """   
    function fiff_write_evoked(name,data,datatype)  
     
    name     filename  
    data     the data structure returned from fiff_read_evoked  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_write_evoked.m)
  """

  return Runtime.call("fiff_write_evoked", *args, **kwargs, nargout=0)
