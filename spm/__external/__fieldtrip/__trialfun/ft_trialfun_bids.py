from spm.__wrapper__ import Runtime


def ft_trialfun_bids(*args, **kwargs):
    """
      FT_TRIALFUN_BIDS determines trials/segments to be used for subsequent analysis, on  
        the basis of the BIDS "events.tsv" file. This function should in general not be  
        called directly, it will be called by FT_DEFINETRIAL.  
         
        Use this function by calling  
          [cfg] = ft_definetrial(cfg)  
        where the configuration structure should contain  
          cfg.dataset   = string with the filename  
          cfg.trialdef  = structure with the details of trial definition, see below  
          cfg.trialfun  = 'ft_trialfun_bids'  
         
        The trialdef structure should either contain the following  
          cfg.trialdef.prestim    = latency in seconds  
          cfg.trialdef.poststim   = latency in seconds  
        or the duration and offset relative to the event of interest  
          cfg.trialdef.duration    = latency in seconds  
          cfg.trialdef.offset      = latency in seconds  
         
        You can specify your selection of events as  
          cfg.trialdef.columnname = columnvalue  
        where the column name and value have to match those present in the events.tsv file.  
         
        For example  
          cfg.trialdef.prestim  = 0.2;  
          cfg.trialdef.poststim = 0.8;  
          cfg.trialdef.task     = 'notarget';  
          cfg.trialdef.category = 'tools';  
          cfg.trialdef.modality = {'written', 'spoken'};  
         
        See also FT_DEFINETRIAL, FT_TRIALFUN_GENERAL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/trialfun/ft_trialfun_bids.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_trialfun_bids", *args, **kwargs)
