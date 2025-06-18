from mpython import Runtime


def _read_ahdf5_hdr(*args, **kwargs):
    """
     read header


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ahdf5_hdr.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_ahdf5_hdr", *args, **kwargs)
