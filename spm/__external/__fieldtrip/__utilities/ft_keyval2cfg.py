from spm.__wrapper__ import Runtime


def ft_keyval2cfg(*args, **kwargs):
    """
      FT_KEYVAL2CFG converts between a structure and a cell-array with key-value  
        pairs which can be used for optional input arguments.   
          
        Use as  
          [cfg] = ft_keyval2cfg(varargin)  
         
        See also FT_CFG2KEYVAL, FT_GETOPT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_keyval2cfg.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_keyval2cfg", *args, **kwargs)
