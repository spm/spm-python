from spm._runtime import Runtime


def _timestamp_plexon(*args, **kwargs):
    r"""
      TIMESTAMP_PLEXON merge the low and high part of the timestamps  
        into a single uint64 value  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/timestamp_plexon.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("timestamp_plexon", *args, **kwargs)
