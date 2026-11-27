from spm._runtime import Runtime


def _read_shm_data(*args, **kwargs):
    r"""
      READ_SHM_DATA reads the data in real-time from shared memory  
        this is a helper function for READ_DATA  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_shm_data.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_shm_data", *args, **kwargs)
