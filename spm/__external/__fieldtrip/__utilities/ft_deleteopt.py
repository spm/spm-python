from spm._runtime import Runtime


def ft_deleteopt(*args, **kwargs):
    r"""
      FT_DELETEOPT removes one or more keys and their corresponding values from a  
        configuration structure or from a cell-array with key-value pairs. It will   
        ignore keys that are not in the structure/cell-array.  
         
        Use as  
          s = ft_deleteopt(s, keys)  
        where s is a structure or a cell-array, and keys is a cell-array or char.  
         
        See also FT_GETOPT, FT_CHECKOPT, FT_SETOPT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/ft_deleteopt.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_deleteopt", *args, **kwargs)
