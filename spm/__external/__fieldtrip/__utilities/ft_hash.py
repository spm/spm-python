from spm._runtime import Runtime


def ft_hash(*args, **kwargs):
    r"""
      FT_HASH computes a MD5 hash from a MATLAB variable or structure  
         
        It will first try a hashing algorithm implemented as a mex file.  
        If that fails, it falls back to a slower one that is based on Java.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/ft_hash.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_hash", *args, **kwargs)
