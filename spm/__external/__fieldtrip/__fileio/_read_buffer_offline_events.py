from spm._runtime import Runtime


def _read_buffer_offline_events(*args, **kwargs):
    r"""
      function E = read_buffer_offline_events(eventfile, header)  
         
        This function reads FCDC buffer-type events from a binary file.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_buffer_offline_events.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_buffer_offline_events", *args, **kwargs)
