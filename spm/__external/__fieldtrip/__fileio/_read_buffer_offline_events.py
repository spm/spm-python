from spm.__wrap__ import _Runtime


def _read_buffer_offline_events(*args, **kwargs):
  """  function E = read_buffer_offline_events(eventfile, header)  
     
    This function reads FCDC buffer-type events from a binary file.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_buffer_offline_events.m)
  """

  return _Runtime.call("read_buffer_offline_events", *args, **kwargs)
