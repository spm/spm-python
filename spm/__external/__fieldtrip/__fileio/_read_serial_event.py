from spm._runtime import Runtime


def _read_serial_event(*args, **kwargs):
    r"""
      READ_SERIAL_EVENT  
         
        changed A.Hadjipapas 2010  
         
        The only thing transmitted is the event.value (no info about sample) but it works  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_serial_event.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_serial_event", *args, **kwargs)
