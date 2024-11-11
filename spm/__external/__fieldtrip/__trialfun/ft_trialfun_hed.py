from spm.__wrapper__ import Runtime


def ft_trialfun_hed(*args, **kwargs):
    """
      FT_TRIALFUN_HED is a trial function that can be used with HED tags. It demonstrates  
        some basic functionality for selecting specific events, but mainly serves as an  
        example or template for your own conditial trial definitions. For that you would  
        copy this function and giuve it your own name, e.g. FT_TRIALFUN_MYEXPERIMENT.  
         
        Use this function by calling  
          [cfg] = ft_definetrial(cfg)  
        where the configuration structure should contain  
          cfg.dataset           = string with the filename  
          cfg.trialfun          = 'ft_trialfun_hed' % or your own copy  
         
        The selection of events and timing of the epochs is specified with  
          cfg.trialdef.regexp     = regular expression that is applied to the HED tags  
          cfg.trialdef.prestim    = number, in seconds  
          cfg.trialdef.poststim   = number, in seconds  
         
        See also FT_DEFINETRIAL, FT_TRIALFUN_GENERAL, FT_TRIALFUN_EXAMPLE1,  
        FT_TRIALFUN_EXAMPLE2  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/trialfun/ft_trialfun_hed.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_trialfun_hed", *args, **kwargs)
