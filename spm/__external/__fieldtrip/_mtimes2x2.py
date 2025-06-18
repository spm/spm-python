from mpython import Runtime


def _mtimes2x2(*args, **kwargs):
    """
      MTIMES2X2 compute x*y where the dimensionatity is 2x2xN or 2x2xNxM


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/mtimes2x2.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mtimes2x2", *args, **kwargs)
