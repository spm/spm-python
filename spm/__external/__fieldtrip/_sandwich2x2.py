from mpython import Runtime


def _sandwich2x2(*args, **kwargs):
    """
      SANDWICH2X2 compute x*y*x' provided y is Hermitian and dimensionality is 2x2xN


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/sandwich2x2.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("sandwich2x2", *args, **kwargs)
