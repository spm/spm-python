from spm.__wrap__ import _Runtime


def fiff_read_raw_segment(*args, **kwargs):
  """   
    [data,times] = fiff_read_raw_segment(raw,from,to,sel)  
     
    Read a specific raw data segment  
     
    raw    - structure returned by fiff_setup_read_raw  
    from   - first sample to include. If omitted, defaults to the  
             first sample in data  
    to     - last sample to include. If omitted, defaults to the last  
             sample in data  
    sel    - optional channel selection vector  
     
    data   - returns the data matrix (channels x samples)  
    times  - returns the time values corresponding to the samples (optional)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_read_raw_segment.m)
  """

  return _Runtime.call("fiff_read_raw_segment", *args, **kwargs)
