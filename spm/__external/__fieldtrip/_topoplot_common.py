from spm.__wrapper__ import Runtime


def _topoplot_common(*args, **kwargs):
    """
      TOPOPLOT_COMMON is shared by FT_TOPOPLOTTFR, FT_TOPOPLOTER and FT_TOPOPLOTIC, which  
        serve as placeholder for the documentation and for the pre/postamble.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/topoplot_common.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("topoplot_common", *args, **kwargs)
