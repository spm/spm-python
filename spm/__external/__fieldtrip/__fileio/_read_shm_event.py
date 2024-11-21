from spm.__wrapper__ import Runtime


def _read_shm_event(*args, **kwargs):
    """
      READ_SHM_EVENT reads the events in real-time from shared memory  
        this is a helper function for READ_EVENT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_shm_event.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_shm_event", *args, **kwargs)
