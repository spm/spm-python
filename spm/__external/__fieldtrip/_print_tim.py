from spm._runtime import Runtime


def _print_tim(*args, **kwargs):
    r"""
      SUBFUNCTION for pretty-printing time in hours, minutes, ...  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/print_tim.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("print_tim", *args, **kwargs)
