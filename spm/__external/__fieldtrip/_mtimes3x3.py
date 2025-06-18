from mpython import Runtime


def _mtimes3x3(*args, **kwargs):
    """
      MTIMES3X3 compute x*y where the dimensionatity is 3x3xN or 3x3xNxM


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/mtimes3x3.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mtimes3x3", *args, **kwargs)
