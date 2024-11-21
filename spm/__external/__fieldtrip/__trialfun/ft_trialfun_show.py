from spm.__wrapper__ import Runtime


def ft_trialfun_show(*args, **kwargs):
    """
      FT_TRIALFUN_SHOW will show a summary of the event information on screen. It will  
        not return an actual trial definition. This function should in general not be  
        called directly, it will be called by FT_DEFINETRIAL.  
         
        Use this function by calling  
          [cfg] = ft_definetrial(cfg)  
        where the configuration structure should contain  
          cfg.dataset   = string with the filename  
          cfg.trialfun  = 'ft_trialfun_show'  
         
        See also FT_DEFINETRIAL, FT_TRIALFUN_GENERAL, FT_TRIALFUN_GUI  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/trialfun/ft_trialfun_show.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_trialfun_show", *args, **kwargs)
