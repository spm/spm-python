from spm.__wrap__ import _Runtime


def _read_sbin_events(*args, **kwargs):
  """  READ_SBIN_EVENTS reads the events information from an EGI segmented simple binary format file  
     
    Use as  
      [EventCodes, segHdr, eventData] = read_sbin_events(filename)  
    with  
      EventCodes      - if NEvent (from header_array) != 0, then array of 4-char event names  
      segHdr          - condition codes and time stamps for each segment  
      eventData       - if NEvent != 0 then event state for each sample, else 'none'  
    and  
      filename    - the name of the data file  
   _______________________________________________________________________  
     
     
    Modified from EGI's readEGLY.m with permission 2008-03-31 Joseph Dien  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_sbin_events.m)
  """

  return _Runtime.call("read_sbin_events", *args, **kwargs)
