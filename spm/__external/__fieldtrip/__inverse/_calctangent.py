from mpython import Runtime


def _calctangent(*args, **kwargs):
    """
      Based on calcrads.m, only difference is that RDip is alread
        with respect to the sphere origin in calctangent.m
        MODIFIED 13th JAN 2005 MATT BROOKES


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/inverse/private/calctangent.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("calctangent", *args, **kwargs)
