from spm.__wrap__ import _Runtime


def ft_multiplotCC(*args, **kwargs):
  """  FT_MULTIPLOTCC visualises the coherence between channels by using  
    multiple topoplots. The topoplot at a given channel location shows the  
    coherence of that channel with all other channels.  
     
    Use as  
      ft_multiplotCC(cfg, data)  
     
    See also FT_PREPARE_LAYOUT, FT_TOPOPLOTCC, FT_CONNECTIVITYPLOT  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/ft_multiplotCC.m)
  """

  return _Runtime.call("ft_multiplotCC", *args, **kwargs)
