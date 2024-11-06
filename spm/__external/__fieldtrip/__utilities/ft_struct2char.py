from spm.__wrapper__ import Runtime


def ft_struct2char(*args, **kwargs):
    """
      FT_STRUCT2CHAR converts all string elements in a structure  
        into char-arrays.  
         
        Use as  
          x = ft_struct2char(x)  
         
        See also FT_STRUCT2STRING, FT_STRUCT2SINGLE, FT_STRUCT2DOUBLE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_struct2char.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_struct2char", *args, **kwargs)
