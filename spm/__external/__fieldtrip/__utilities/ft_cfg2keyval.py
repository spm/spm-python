from spm._runtime import Runtime


def ft_cfg2keyval(*args, **kwargs):
    r"""
      FT_CFG2KEYVAL converts between a structure and a cell-array with key-value  
        pairs which can be used for optional input arguments.  
         
        Use as  
          optarg = ft_cfg2keyval(cfg)  
         
        See also FT_KEYVAL2CFG, FT_GETOPT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/ft_cfg2keyval.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_cfg2keyval", *args, **kwargs)
