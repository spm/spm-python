from spm.__wrapper__ import Runtime


def ft_trialfun_example1(*args, **kwargs):
    """
      FT_TRIALFUN_EXAMPLE1 is an example trial function. It searches for events  
        of type "trigger" and specifically for a trigger with value 7, followed  
        by a trigger with value 64.  
         
        You can use this as a template for your own conditial trial definitions.  
         
        Use this function by calling  
          [cfg] = ft_definetrial(cfg)  
        where the configuration structure should contain  
          cfg.dataset           = string with the filename  
          cfg.trialfun          = 'ft_trialfun_example1'  
          cfg.trialdef.prestim  = number, in seconds  
          cfg.trialdef.poststim = number, in seconds  
         
        See also FT_DEFINETRIAL, FT_TRIALFUN_GENERAL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/trialfun/ft_trialfun_example1.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_trialfun_example1", *args, **kwargs)
