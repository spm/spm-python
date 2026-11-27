from spm._runtime import Runtime


def _ft_struct2json(*args, **kwargs):
    r"""
       FT_STRUCT2JSON  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/ft_struct2json.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_struct2json", *args, **kwargs)
