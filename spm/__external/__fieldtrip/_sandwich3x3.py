from mpython import Runtime


def _sandwich3x3(*args, **kwargs):
    """
      SANDWICH3X3 compute x*y*x' provided y is Hermitian and dimensionality is 3x3xN


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/sandwich3x3.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("sandwich3x3", *args, **kwargs)
