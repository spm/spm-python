from spm._runtime import Runtime


def _timestamp_neuralynx(*args, **kwargs):
    r"""
      TIMESTAMP_NEURALYNX merge the low and high part of Neuralynx timestamps  
        into a single uint64 value  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/timestamp_neuralynx.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("timestamp_neuralynx", *args, **kwargs)
