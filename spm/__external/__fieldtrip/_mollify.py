from mpython import Runtime


def _mollify(*args, **kwargs):
    """
      This function does something


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/mollify.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mollify", *args, **kwargs)
