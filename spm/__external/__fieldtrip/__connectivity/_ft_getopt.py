from spm.__wrapper__ import Runtime


def _ft_getopt(*args, **kwargs):
    """
      FT_GETOPT gets the value of a specified option from a configuration structure  
        or from a cell-array with key-value pairs.  
         
        Use as  
          val = ft_getopt(s, key, default, emptymeaningful)  
        where the input values are  
          s               = structure or cell-array  
          key             = string  
          default         = any valid MATLAB data type (optional, default = [])  
          emptymeaningful = boolean value (optional, default = false)  
         
        If the key is present as field in the structure, or as key-value pair in the  
        cell-array, the corresponding value will be returned.  
         
        If the key is not present, ft_getopt will return the default, or an empty array  
        when no default was specified.  
         
        If the key is present but has an empty value, then the emptymeaningful flag  
        specifies whether the empty value or the default value should be returned.  
        If emptymeaningful==true, then the empty array will be returned.  
        If emptymeaningful==false, then the specified default will be returned.  
         
        See also FT_SETOPT, FT_CHECKOPT, INPUTPARSER  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/private/ft_getopt.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_getopt", *args, **kwargs)
