from mpython import Runtime


def _read_asa_msr(*args, **kwargs):
    """
      READ_ASA_MSR reads EEG or MEG data from an ASA data file
        converting the units to uV or fT


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_asa_msr.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_asa_msr", *args, **kwargs)
