from spm.__wrapper__ import Runtime


def ft_heartrate(*args, **kwargs):
    """
      FT_HEARTRATE estimates the heart rate from a continuous PPG or ECG channel. It  
        returns a new data structure with a continuous representation of the heartrate in  
        beats per minute, the heart period (i.e., the RR interval) in seconds per interval,  
        the heartbeat phase and the moment of the heartbeat onsets.  
         
        Use as  
          dataout = ft_heartrate(cfg, data)  
        where the input data is a structure as obtained from FT_PREPROCESSING and the  
        output is a similar structure with the same trials and time-charactersitics, but  
        with new channels describing the heart rate parameters.  
         
        The configuration structure has the following general options  
          cfg.channel          = selected channel for processing, see FT_CHANNELSELECTION  
          cfg.feedback         = 'yes' or 'no'  
          cfg.method           = string representing the method for heart beat detection  
                                 'findpeaks'  filtering and normalization, followed by FINDPEAKS (default)  
                                 'pantompkin' implementation of the Pan-Tompkin algorithm for ECG beat detection  
         
        For the 'findpeaks' method the following additional options can be specified  
          cfg.envelopewindow   = scalar, time in seconds (default = 10)  
          cfg.peakseparation   = scalar, time in seconds  
          cfg.threshold        = scalar, usually between 0 and 1 (default = 0.4), 'MinPeakHeight' parameter for findpeaks function  
          cfg.mindistance      = scalar, time in seconds for the minimal distance between consecutive peaks (default = 0),   
                                 'MinPeakDistance' for findpeaks functions (after conversion from seconds into samples)  
          cfg.flipsignal       = 'yes' or 'no', whether to flip the polarity of the signal (default is automatic)  
        and the data can be preprocessed on the fly using  
          cfg.preproc.bpfilter = 'yes' or 'no'  
          cfg.preproc.bpfreq   = [low high], filter frequency in Hz  
        This implementation performs some filtering and amplitude normalization, followed  
        by the FINDPEAKS function. It works both for ECG as for PPG signals.  
         
        For the 'pantompkin` method there are no additional options. This implements  
        - J Pan, W J Tompkins, "A Real-Time QRS Detection Algorithm", IEEE Trans Biomed Eng, 1985. https://doi.org/10.1109/tbme.1985.325532  
        - H Sedghamiz, "Matlab Implementation of Pan Tompkins ECG QRS detector". https://doi.org/10.13140/RG.2.2.14202.59841  
         
        You can correct ectopic beats using the following options  
          cfg.ectopicbeatcorrect   = 'yes' or 'no', replace a single ectopic beat (default = 'no')  
          cfg.ectopicbeatthreshold = fractional number as percentage (default = 0.2  
         
        An ectopic beat is a premature ventricual contraction, causing a very short-lived  
        increase in the variability in the rate. This can be corrected by replacing it with  
        a beat that falls exactly in between its neighbouring beats. A beat is detected as  
        ectopic if the RR-interval of a beat is 20% (default) smaller than the previous  
        beat-to-beat interval and is followed by an interval that is 20% (default) larger  
        (i.e. refractory period). The default threshold of 0.2 can be modified with  
        cfg.ectopicbeatthreshold.  
         
        See also FT_ELECTRODERMALACTIVITY, FT_HEADMOVEMENT, FT_REGRESSCONFOUND  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_heartrate.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_heartrate", *args, **kwargs)
