from spm.__wrapper__ import Runtime


def fiff_read_events(*args, **kwargs):
  """   
    [events, mappings] = fiff_read_events(source, tree)  
     
    Read the events  
     
    If tree is specified, source is assumed to be an open file id,  
    otherwise a the name of the file to read. If tree is missing, the  
    meas output argument should not be specified.  
     
     
      Author : Martin Luessi, MGH Martinos Center  
      License : BSD 3-clause  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_read_events.m)
  """

  return Runtime.call("fiff_read_events", *args, **kwargs)
