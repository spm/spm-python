from spm._runtime import Runtime


def ft_trialfun_balert(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/trialfun/ft_trialfun_balert.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_trialfun_balert", *args, **kwargs)
