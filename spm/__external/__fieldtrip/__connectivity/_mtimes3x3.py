from spm._runtime import Runtime


def _mtimes3x3(*args, **kwargs):
    r"""
      MTIMES3X3 compute x*y where the dimensionatity is 3x3xN or 3x3xNxM  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/connectivity/private/mtimes3x3.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mtimes3x3", *args, **kwargs)
