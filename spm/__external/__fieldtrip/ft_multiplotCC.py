from spm._runtime import Runtime


def ft_multiplotCC(*args, **kwargs):
    r"""
      FT_MULTIPLOTCC visualises the coherence between channels by using  
        multiple topoplots. The topoplot at a given channel location shows the  
        coherence of that channel with all other channels.  
         
        Use as  
          ft_multiplotCC(cfg, data)  
         
        See also FT_PREPARE_LAYOUT, FT_TOPOPLOTCC, FT_CONNECTIVITYPLOT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/ft_multiplotCC.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_multiplotCC", *args, **kwargs)
