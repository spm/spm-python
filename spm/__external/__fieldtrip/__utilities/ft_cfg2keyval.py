from spm.__wrapper__ import Runtime


def ft_cfg2keyval(*args, **kwargs):
    """
      FT_CFG2KEYVAL converts between a structure and a cell-array with key-value  
        pairs which can be used for optional input arguments.  
         
        Use as  
          optarg = ft_cfg2keyval(cfg)  
         
        See also FT_KEYVAL2CFG, FT_GETOPT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_cfg2keyval.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_cfg2keyval", *args, **kwargs)
