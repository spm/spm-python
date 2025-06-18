from mpython import Runtime


def _read_asa_elc(*args, **kwargs):
    """
      READ_ASA_ELC reads electrodes from an ASA electrode file
        converting the units to mm


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_asa_elc.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_asa_elc", *args, **kwargs)
