from mpython import Runtime


def _elec1020_intersect(*args, **kwargs):
    """
      ELEC1020_INTERSECT determines the intersection of a mesh with a plane


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/elec1020_intersect.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("elec1020_intersect", *args, **kwargs)
