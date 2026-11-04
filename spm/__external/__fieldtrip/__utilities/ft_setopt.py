from spm._runtime import Runtime


def ft_setopt(*args, **kwargs):
    r"""
      FT_SETOPT assigns a value to an configuration structure or to a cell-array  
        with key-value pairs. It will overwrite the option if already present, or  
        append the option if not present.  
         
        Use as  
          s = ft_setopt(s, key, val)  
        where s is a structure or a cell-array.  
         
        See also FT_GETOPT, FT_CHECKOPT, FT_DELETEOPT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/ft_setopt.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_setopt", *args, **kwargs)
