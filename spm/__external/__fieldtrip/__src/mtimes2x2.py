from spm._runtime import Runtime


def mtimes2x2(*args, **kwargs):
    r"""
      MTIMES2X2 compute x*y where the dimensionatity is 2x2xN or 2x2xNxM  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/src/mtimes2x2.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mtimes2x2", *args, **kwargs)
