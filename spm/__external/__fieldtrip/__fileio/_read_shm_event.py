from spm._runtime import Runtime


def _read_shm_event(*args, **kwargs):
    r"""
      READ_SHM_EVENT reads the events in real-time from shared memory  
        this is a helper function for READ_EVENT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_shm_event.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_shm_event", *args, **kwargs)
