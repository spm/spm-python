from spm._runtime import Runtime


def ft_struct2string(*args, **kwargs):
    r"""
      FT_STRUCT2STRING converts all char-array elements in a structure  
        into strings.  
         
        Use as  
          x = ft_struct2string(x)  
         
        See also FT_STRUCT2CHAR, FT_STRUCT2SINGLE, FT_STRUCT2DOUBLE  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/ft_struct2string.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_struct2string", *args, **kwargs)
