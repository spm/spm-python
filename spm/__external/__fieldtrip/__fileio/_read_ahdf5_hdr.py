from spm._runtime import Runtime


def _read_ahdf5_hdr(*args, **kwargs):
    r"""
     read header  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_ahdf5_hdr.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_ahdf5_hdr", *args, **kwargs)
