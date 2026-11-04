from spm._runtime import Runtime


def _topoplot_common(*args, **kwargs):
    r"""
      TOPOPLOT_COMMON is shared by FT_TOPOPLOTTFR, FT_TOPOPLOTER and FT_TOPOPLOTIC, which  
        serve as placeholder for the documentation and for the pre/postamble.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/topoplot_common.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("topoplot_common", *args, **kwargs)
