from spm._runtime import Runtime


def _join_str(*args, **kwargs):
    r"""
    join_str is a function.  
          t = join_str(separator, cells)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/join_str.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("join_str", *args, **kwargs)
