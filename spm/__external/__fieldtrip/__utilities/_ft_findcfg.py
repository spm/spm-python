from spm._runtime import Runtime


def _ft_findcfg(*args, **kwargs):
    r"""
      FT_FINDCFG searches for an element in the cfg structure  
        or in the nested previous cfgs  
         
        Use as  
          val = ft_findcfg(cfg, var)  
        where the name of the variable should be specified as string.  
         
        e.g.  
          trl   = ft_findcfg(cfg, 'trl')  
          event = ft_findcfg(cfg, 'event')  
         
        See also FT_GETOPT, FT_CFG2KEYVAL  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/ft_findcfg.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_findcfg", *args, **kwargs)
