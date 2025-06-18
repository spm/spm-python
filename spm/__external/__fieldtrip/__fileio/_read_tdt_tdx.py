from mpython import Runtime


def _read_tdt_tdx(*args, **kwargs):
    """
      tdx file contains just information about epoc,
        is generated after recording if necessary for fast retrieve epoc information


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_tdt_tdx.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_tdt_tdx", *args, **kwargs)
