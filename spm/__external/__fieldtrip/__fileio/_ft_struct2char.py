from spm._runtime import Runtime


def _ft_struct2char(*args, **kwargs):
    r"""
      FT_STRUCT2CHAR converts all string elements in a structure  
        into char-arrays.  
         
        Use as  
          x = ft_struct2char(x)  
         
        See also FT_STRUCT2STRING, FT_STRUCT2SINGLE, FT_STRUCT2DOUBLE  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/ft_struct2char.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_struct2char", *args, **kwargs)
