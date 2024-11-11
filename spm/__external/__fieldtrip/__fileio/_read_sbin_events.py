from spm.__wrapper__ import Runtime


def _read_sbin_events(*args, **kwargs):
    """
      READ_SBIN_EVENTS reads the events information from an EGI segmented simple binary format file  
         
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_sbin_events.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_sbin_events", *args, **kwargs)
