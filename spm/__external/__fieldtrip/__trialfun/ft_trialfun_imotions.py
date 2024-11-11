from spm.__wrapper__ import Runtime


def ft_trialfun_imotions(*args, **kwargs):
    """
      FT_TRIALFUN_IMOTIONS makes a trial definition for an iMotions event structure.  
        Note that this returns the trial definition as a table rather than as a numeric array.  
         
        Use this function by calling  
          [cfg] = ft_definetrial(cfg)  
        where the configuration structure should contain  
          cfg.event               = event structure  
          cfg.fsample             = number, samplijng rate in Hz  
          cfg.trialfun            = 'ft_trialfun_imotions'  
          cfg.trialdef.eventtype  = string or cell-array of strings (default = 'StimulusName')  
          cfg.trialdef.eventvalue = string or cell-array of strings (default = [])  
          cfg.trialdef.offset     = string, 'absolute' or 'relative' (default = 'absolute')  
         
        See also FT_DEFINETRIAL, FT_TRIALFUN_GENERAL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/trialfun/ft_trialfun_imotions.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_trialfun_imotions", *args, **kwargs)
