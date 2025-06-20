from spm._runtime import Runtime


def _read_shm_header(*args, **kwargs):
    """
      READ_SHM_HEADER reads the header in real-time from shared memory  
        this is a helper function for FT_READ_HEADER  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_shm_header.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_shm_header", *args, **kwargs)
