from spm._runtime import Runtime


def _size_equal(*args, **kwargs):
    r"""
      returns true if all input arguments are equal to each other  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/external/stats/private/size_equal.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("size_equal", *args, **kwargs)
