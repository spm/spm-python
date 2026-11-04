from spm._runtime import Runtime


def _rejectvisual_summary(*args, **kwargs):
    r"""
      SUBFUNCTION for ft_rejectvisual  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/rejectvisual_summary.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("rejectvisual_summary", *args, **kwargs)
