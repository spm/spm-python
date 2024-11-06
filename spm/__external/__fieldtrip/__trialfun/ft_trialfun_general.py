from spm.__wrapper__ import Runtime


def ft_trialfun_general(*args, **kwargs):
    """
      FT_TRIALFUN_GENERAL reads events from the dataset using FT_READ_EVENT and  
        constructs a trial definition. This function should in general not be called  
        directly, it will be called by FT_DEFINETRIAL.  
         
        Use this function by calling  
          [cfg] = ft_definetrial(cfg)  
        where the configuration structure should contain  
          cfg.dataset   = string with the filename  
          cfg.trialdef  = structure with the details of trial definition, see below  
          cfg.trialfun  = 'ft_trialfun_general'  
         
        The cfg.trialdef structure can contain the following specifications  
          cfg.trialdef.eventtype  = string, or cell-array with strings  
          cfg.trialdef.eventvalue = number, string, or list with numbers or strings  
          cfg.trialdef.prestim    = number, latency in seconds (optional)  
          cfg.trialdef.poststim   = number, latency in seconds (optional)  
         
        You can specify these options that are passed to FT_READ_EVENT for trigger detection  
          cfg.trialdef.detectflank  = string, can be 'up', 'updiff', 'down', 'downdiff', 'both', 'any', 'biton', 'bitoff'  
          cfg.trialdef.trigshift    = integer, number of samples to shift from flank to detect trigger value  
          cfg.trialdef.chanindx     = list with channel numbers for the trigger detection, specify -1 in case you don't want to detect triggers  
          cfg.trialdef.threshold    = threshold for analog trigger channels  
          cfg.trialdef.tolerance    = tolerance in samples when merging analogue trigger channels, only for Neuromag  
         
        If you want to read all data from a continuous file in segments, you can specify  
           cfg.trialdef.length      = duration of the segments in seconds (can be Inf)  
           cfg.trialdef.ntrials     = number of trials (optional, can be 1)  
           cfg.trialdef.overlap     = single number (between 0 and 1 (exclusive)) specifying the fraction of overlap between snippets (0 = no overlap)  
         
        See also FT_DEFINETRIAL, FT_TRIALFUN_GUI, FT_TRIALFUN_SHOW  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/trialfun/ft_trialfun_general.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_trialfun_general", *args, **kwargs)
