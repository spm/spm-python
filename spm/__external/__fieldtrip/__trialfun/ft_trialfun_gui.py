from spm.__wrapper__ import Runtime


def ft_trialfun_gui(*args, **kwargs):
    """
      FT_TRIALFUN_GUI reads events from the dataset, displays a graphical user interface  
        dialog to select the event types and values of interest, and constructs a trial  
        definition. This function should in general not be called directly, it will be  
        called by FT_DEFINETRIAL.  
         
        Use this function by calling  
          [cfg] = ft_definetrial(cfg)  
        where the configuration structure should contain  
          cfg.dataset   = string with the filename  
          cfg.trialfun  = 'ft_trialfun_gui'  
         
        See also FT_DEFINETRIAL, FT_TRIALFUN_GENERAL, FT_TRIALFUN_SHOW  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/trialfun/ft_trialfun_gui.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_trialfun_gui", *args, **kwargs)
