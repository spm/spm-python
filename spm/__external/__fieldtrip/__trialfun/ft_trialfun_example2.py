from spm.__wrapper__ import Runtime


def ft_trialfun_example2(*args, **kwargs):
    """
      FT_TRIALFUN_EXAMPLE2 is an example trial function that detects muscle activity in  
        an EMG channel and defines variable length trials from the EMG onset up to the EMG  
        offset.  
         
        Use this function by calling  
          [cfg] = ft_definetrial(cfg)  
        where the configuration structure should contain  
          cfg.dataset           = string with the filename  
          cfg.trialfun          = 'ft_trialfun_example2'  
         
        Note that there are some parameters, like the EMG channel name and the processing  
        that is done on the EMG channel data, which are hardcoded in this trial function.  
        You should change these parameters according to your data.  
         
        See also FT_DEFINETRIAL, FT_TRIALFUN_GENERAL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/trialfun/ft_trialfun_example2.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_trialfun_example2", *args, **kwargs)
