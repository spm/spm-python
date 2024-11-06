from spm.__wrapper__ import Runtime


def ft_trialfun_edf(*args, **kwargs):
    """
      FT_TRIALFUN_EDF is an example trial function for EDF data. It searches for events  
        of type "up" in an analog data channel, as indentified by thresholding. This  
        threshold can be a hard threshold, i.e. a numeric, or can flexibly be defined  
        depending on the data, for example calculating the 'median' of an analog signal.  
         
        You can use this as a template for your own conditial trial definitions.  
         
        Use this function by calling   
          [cfg] = ft_definetrial(cfg)  
        where the configuration structure should contain  
          cfg.dataset  = string with the filename  
          cfg.trialfun = 'ft_trialfun_edf'  
         
        See also FT_DEFINETRIAL, FT_TRIALFUN_GENERAL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/trialfun/ft_trialfun_edf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_trialfun_edf", *args, **kwargs)
