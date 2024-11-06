from spm.__wrapper__ import Runtime


def ft_respiration(*args, **kwargs):
    """
      FT_RESPIRATION estimates the respiration rate from a respiration belt, temperature  
        sensor, movement sensor or from the heart rate. It returns a new data structure  
        with a continuous representation of the rate and phase.  
         
        Use as  
          dataout = ft_respiration(cfg, data)  
        where the input data is a structure as obtained from FT_PREPROCESSING.  
         
        The configuration structure has the following options  
          cfg.channel          = selected channel for processing, see FT_CHANNELSELECTION  
          cfg.peakseparation   = scalar, time in seconds  
          cfg.envelopewindow   = scalar, time in seconds  
          cfg.feedback         = 'yes' or 'no'  
        The input data can be preprocessed on the fly using  
          cfg.preproc.bpfilter = 'yes' or 'no' (default = 'yes')  
          cfg.preproc.bpfreq   = [low high], filter frequency in Hz  
         
        See also FT_HEARTRATE, FT_ELECTRODERMALACTIVITY, FT_HEADMOVEMENT, FT_REGRESSCONFOUND  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_respiration.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_respiration", *args, **kwargs)
