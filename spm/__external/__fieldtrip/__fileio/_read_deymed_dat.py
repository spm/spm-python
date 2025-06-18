from mpython import Runtime


def _read_deymed_dat(*args, **kwargs):
    """
      READ_DEYMED_DAT reads EEG data from the Deymed Truescan file format

        Use as
          dat = read_deymed_dat(filename, hdr, begsample, endsample)

        See also READ_DEYMED_INI


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_deymed_dat.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_deymed_dat", *args, **kwargs)
