from mpython import Runtime


def _cstructdecode(*args, **kwargs):
    """
      CSTRUCTDECODE decodes a structure from a uint8 buffer

        See READ_NEURALYNX_NEV for an example


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/cstructdecode.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cstructdecode", *args, **kwargs)
