from spm._runtime import Runtime


def _fixoldorg(*args, **kwargs):
    r"""
      FIXOLDORG use "old/new" instead of "org/new"  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/fixoldorg.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fixoldorg", *args, **kwargs)
