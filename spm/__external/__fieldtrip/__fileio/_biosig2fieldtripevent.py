from mpython import Runtime


def _biosig2fieldtripevent(*args, **kwargs):
    """
      BIOSIG2FIELDTRIPEVENT converts event information from a biosig hdr into
        fieldtrip events


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/biosig2fieldtripevent.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("biosig2fieldtripevent", *args, **kwargs)
