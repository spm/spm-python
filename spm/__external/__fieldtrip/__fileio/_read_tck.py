from mpython import Runtime


def _read_tck(*args, **kwargs):
    """
      READ_TCK reads tractography information from an mrtrix-generated .tck
        file. Requires the matlab functions from mrtrix.


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_tck.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_tck", *args, **kwargs)
