from spm._runtime import Runtime


def sandwich2x2(*args, **kwargs):
    r"""
      SANDWICH2X2 compute x*y*x' provided y is Hermitian and dimensionality is 2x2xN  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/src/sandwich2x2.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("sandwich2x2", *args, **kwargs)
