from spm.__wrapper__ import Runtime


def ft_trialfun_neuromagSTI016fix(*args, **kwargs):
    """
      FT_TRIALFUN_NEUROMAGSTI106FIX is supposed to fix the error with STI016 in  
        Neuromag/Elekta/MEGIN data. It reads the channels STI001 up to STI016, combines the  
        values into a new "STI101" channel and then uses the new channel to define trials.  
         
        Use this function by calling  
          [cfg] = ft_definetrial(cfg)  
        where the configuration structure should contain  
          cfg.dataset             = string, containing filename or directory  
          cfg.trialdef.prestim    = pre stimulus time in s  
          cfg.trialdef.poststim   = post stimulus time in seconds  
          cfg.trialdef.eventvalue = list with trigger values  
          cfg.trialfun            = 'ft_trialfun_neuromagSTI016fix';  
         
        See also FT_DEFINETRIAL, FT_TRIALFUN_GENERAL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/trialfun/ft_trialfun_neuromagSTI016fix.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_trialfun_neuromagSTI016fix", *args, **kwargs)
