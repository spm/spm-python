from spm._runtime import Runtime


def _ft_setopt(*args, **kwargs):
    """
      FT_SETOPT assigns a value to an configuration structure or to a cell-array  
        with key-value pairs. It will overwrite the option if already present, or  
        append the option if not present.  
         
        Use as  
          s = ft_setopt(s, key, val)  
        where s is a structure or a cell-array.  
         
        See also FT_GETOPT, FT_CHECKOPT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/inverse/private/ft_setopt.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_setopt", *args, **kwargs)
