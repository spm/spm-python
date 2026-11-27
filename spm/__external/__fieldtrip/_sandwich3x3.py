from spm._runtime import Runtime


def _sandwich3x3(*args, **kwargs):
    r"""
      SANDWICH3X3 compute x*y*x' provided y is Hermitian and dimensionality is 3x3xN  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/sandwich3x3.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("sandwich3x3", *args, **kwargs)
