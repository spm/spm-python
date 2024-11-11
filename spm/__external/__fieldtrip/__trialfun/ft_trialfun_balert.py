from spm.__wrapper__ import Runtime


def ft_trialfun_balert(*args, **kwargs):
    """
      FT_TRIALFUN_BALERT extract trials from B-Alert data using an intermediate CSV file.  
        FieldTrip cannot yet directly interpret the event markers from B-Alert data.  
        Therefore, it is necessary to have B-Alert LAB. This is (paid) software from  
        Advanced Brain Monitoring, in which you extract the eventmakers using the function:  
        readevents(*.Events.edf, *.Signals.Raw.edf) to write a *.csv file.  
         
        Use this function by calling  
          [cfg] = ft_definetrial(cfg)  
        where the configuration structure should contain  
          cfg.dataset = string with the *.csv filename  
          cfg.trialfun = 'ft_trialfun_balert'  
         
        See also FT_DEFINETRIAL, FT_PREPROCESSING  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/trialfun/ft_trialfun_balert.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_trialfun_balert", *args, **kwargs)
