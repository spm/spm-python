from spm._runtime import Runtime


def _defaultId(*args, **kwargs):
    """
      DEFAULTID returns a string that can serve as warning or error identifier,  
        for example 'FieldTip:ft_read_header:line345'.  
         
        See also WARNING, ERROR, FT_NOTICE, FT_INFO, FT_DEBUG  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/defaultId.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("defaultId", *args, **kwargs)
