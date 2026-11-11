from spm._runtime import Runtime


def _guidelines(*args, **kwargs):
    r"""
      GUIDELINES searches for a contiguous block of commented text and shows  
        its contents. It is used to display additional help sections.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/guidelines.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("guidelines", *args, **kwargs)
