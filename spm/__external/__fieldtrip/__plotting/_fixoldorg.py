from mpython import Runtime


def _fixoldorg(*args, **kwargs):
    """
      FIXOLDORG use "old/new" instead of "org/new"


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/fixoldorg.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fixoldorg", *args, **kwargs)
