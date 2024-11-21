from spm.__wrapper__ import Runtime


def _read_shm_data(*args, **kwargs):
    """
      READ_SHM_DATA reads the data in real-time from shared memory  
        this is a helper function for READ_DATA  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_shm_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_shm_data", *args, **kwargs)
