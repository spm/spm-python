from spm._runtime import Runtime


def _ft_urlread(*args, **kwargs):
    r"""
      FT_URLREAD  
         
        The documentation of R2016b states that urlread is not recommended.  
        Use webread or webwrite instead.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/ft_urlread.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_urlread", *args, **kwargs)
