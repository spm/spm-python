from spm.__wrap__ import _Runtime


def _ft_findcfg(*args, **kwargs):
  """  FT_FINDCFG searches for an element in the cfg structure  
    or in the nested previous cfgs  
     
    Use as  
      val = ft_findcfg(cfg, var)  
    where the name of the variable should be specified as string.  
     
    e.g.  
      trl   = ft_findcfg(cfg, 'trl')  
      event = ft_findcfg(cfg, 'event')  
     
    See also FT_GETOPT, FT_CFG2KEYVAL  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/ft_findcfg.m)
  """

  return _Runtime.call("ft_findcfg", *args, **kwargs)
