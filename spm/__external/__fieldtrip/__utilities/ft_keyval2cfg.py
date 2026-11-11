from spm._runtime import Runtime


def ft_keyval2cfg(*args, **kwargs):
    r"""
      FT_KEYVAL2CFG converts between a structure and a cell-array with key-value  
        pairs which can be used for optional input arguments.   
          
        Use as  
          [cfg] = ft_keyval2cfg(varargin)  
         
        See also FT_CFG2KEYVAL, FT_GETOPT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/ft_keyval2cfg.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_keyval2cfg", *args, **kwargs)
