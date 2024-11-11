from spm.__wrapper__ import Runtime


def ft_electrodermalactivity(*args, **kwargs):
    """
      FT_ELECTRODERMALACTIVITY estimates the electrodermal activity from a recording of  
        the electric resistance of the skin.  
         
        Use as  
          eda = ft_electrodermalactivity(cfg, data)  
        where the input data is a structure as obtained from FT_PREPROCESSING.  
         
        The configuration structure has the following options  
          cfg.channel        = selected channel for processing, see FT_CHANNELSELECTION  
          cfg.feedback       = 'yes' or 'no'  
          cfg.medianwindow   = scalar, length of window for median filter in seconds (default = 8)  
         
        After using this function you can use FT_REDEFINETRIAL and FT_TIMELOCKANLAYSIS to  
        investigate electrodermal responses (EDRs) to stimulation. You can use  
        FT_ARTIFACT_THRESHOLD to determine the timing and frequency of nonspecific EDRs.  
         
        See https://doi.org/10.1111/j.1469-8986.2012.01384.x "Publication recommendations  
        for electrodermal measurements" by the SPR for an introduction in electrodermal  
        methods and for recommendations.  
         
        See also FT_HEARTRATE, FT_HEADMOVEMENT, FT_REGRESSCONFOUND  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_electrodermalactivity.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_electrodermalactivity", *args, **kwargs)
