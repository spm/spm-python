from spm._runtime import Runtime


def _elec1020_intersect(*args, **kwargs):
    r"""
      ELEC1020_INTERSECT determines the intersection of a mesh with a plane  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/elec1020_intersect.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("elec1020_intersect", *args, **kwargs)
