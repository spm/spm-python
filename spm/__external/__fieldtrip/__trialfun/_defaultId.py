from spm._runtime import Runtime


def _defaultId(*args, **kwargs):
    r"""
      DEFAULTID returns a string that can serve as warning or error identifier,  
        for example 'FieldTip:ft_read_header:line345'.  
         
        See also WARNING, ERROR, FT_NOTICE, FT_INFO, FT_DEBUG  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/trialfun/private/defaultId.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("defaultId", *args, **kwargs)
