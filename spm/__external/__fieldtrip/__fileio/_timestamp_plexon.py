from spm.__wrapper__ import Runtime


def _timestamp_plexon(*args, **kwargs):
    """
      TIMESTAMP_PLEXON merge the low and high part of the timestamps  
        into a single uint64 value  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/timestamp_plexon.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("timestamp_plexon", *args, **kwargs)
