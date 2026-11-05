from spm._runtime import Runtime


def _checktime(*args, **kwargs):
    r"""
      last input is always the required string  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/checktime.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("checktime", *args, **kwargs)
