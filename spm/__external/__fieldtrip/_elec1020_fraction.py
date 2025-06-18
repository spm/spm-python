from mpython import Runtime


def _elec1020_fraction(*args, **kwargs):
    """
      ELEC1020_FRACTION


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/elec1020_fraction.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("elec1020_fraction", *args, **kwargs)
