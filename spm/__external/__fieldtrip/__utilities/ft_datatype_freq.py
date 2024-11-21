from spm.__wrapper__ import Runtime


def ft_datatype_freq(*args, **kwargs):
    """
      FT_DATATYPE_FREQ describes the FieldTrip MATLAB structure for freq data  
         
        The freq data structure represents frequency or time-frequency decomposed  
        channel-level data. This data structure is usually generated with the  
        FT_FREQANALYSIS function.  
         
        An example of a freq data structure containing the powerspectrum for 306 channels  
        and 120 frequencies is  
         
              dimord: 'chan_freq'          defines how the numeric data should be interpreted  
           powspctrm: [306x120 double]     the power spectrum  
               label: {306x1 cell}         the channel labels  
                freq: [1x120 double]       the frequencies expressed in Hz  
                 cfg: [1x1 struct]         the configuration used by the function that generated this data structure  
         
        An example of a freq data structure containing the time-frequency resolved  
        spectral estimates of power (i.e. TFR) for 306 channels, 120 frequencies  
        and 60 timepoints is  
         
              dimord: 'chan_freq_time'     defines how the numeric data should be interpreted  
           powspctrm: [306x120x60 double]  the power spectrum  
               label: {306x1 cell}         the channel labels  
                freq: [1x120 double]       the frequencies, expressed in Hz  
                time: [1x60 double]        the time, expressed in seconds  
                 cfg: [1x1 struct]         the configuration used by the function that generated this data structure  
         
        Required fields:  
          - freq, dimord, label or labelcmb  
         
        Optional fields:  
          - powspctrm, fouriesspctrm, csdspctrm, cohspctrm, time, grad, elec, cumsumcnt, cumtapcnt, trialinfo  
         
        Deprecated fields:  
          - <none>  
         
        Obsoleted fields:  
          - <none>  
         
        Revision history:  
         
        (2011/latest) The description of the sensors has changed, see FT_DATATYPE_SENS  
        for further information.  
         
        (2008) The presence of labelcmb in case of crsspctrm became optional,  
        from now on the crsspctrm can also be represented as Nchan * Nchan.  
         
        (2006) The fourierspctrm field was added as alternative to powspctrm and  
        crsspctrm. The fields foi and toi were renamed to freq and time.  
         
        (2003v2) The fields sgn and sgncmb were renamed into label and labelcmb.  
         
        (2003v1) The initial version was defined.  
         
        See also FT_DATATYPE, FT_DATATYPE_COMP, FT_DATATYPE_DIP, FT_DATATYPE_FREQ,  
        FT_DATATYPE_MVAR, FT_DATATYPE_RAW, FT_DATATYPE_SOURCE, FT_DATATYPE_SPIKE,  
        FT_DATATYPE_TIMELOCK, FT_DATATYPE_VOLUME  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_datatype_freq.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_datatype_freq", *args, **kwargs)
