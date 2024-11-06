from spm.__wrapper__ import Runtime


def ft_specest_mtmconvol(*args, **kwargs):
    """
      FT_SPECEST_MTMCONVOL performs wavelet convolution in the time domain by  
        multiplication in the frequency domain.  
         
        Use as  
          [spectrum, ntaper, freqoi, timeoi] = ft_specest_mtmconvol(dat, time, ...)  
        where the input arguments are  
          dat       = matrix of chan*sample  
          time      = vector, containing time in seconds for each sample  
        and the ouitput arguments are  
          spectrum  = matrix of ntaper*chan*freqoi*timeoi of fourier coefficients  
          ntaper    = vector containing the number of tapers per freqoi  
          freqoi    = vector of frequencies in spectrum  
          timeoi    = vector of timebins in spectrum  
         
        Optional arguments should be specified in key-value pairs and can include  
          freqoi    = vector, containing frequencies (in Hz)  
          timeoi    = vector, containing time points of interest (in seconds)  
          timwin    = vector, containing length of time windows (in seconds)  
          taper     = 'dpss', 'hanning' or many others, see WINDOW (default = 'dpss')  
          taperopt  = additional taper options to be used in the WINDOW function, see WINDOW  
          tapsmofrq = number, the amount of spectral smoothing through multi-tapering. Note: 4 Hz smoothing means plus-minus 4 Hz, i.e. a 8 Hz smoothing box  
          pad       = number, indicating time-length of data to be padded out to in seconds  
          padtype   = string, indicating type of padding to be used (see ft_preproc_padding, default: zero)  
          dimord    = 'tap_chan_freq_time' (default) or 'chan_time_freqtap' for memory efficiency  
          polyorder = number, the order of the polynomial to fitted to and removed from the data prior to the fourier transform (default = 0 -> remove DC-component)  
          verbose   = output progress to console (0 or 1, default 1)  
         
        See also FT_FREQANALYSIS, FT_SPECEST_MTMFFT, FT_SPECEST_TFR, FT_SPECEST_HILBERT, FT_SPECEST_WAVELET  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/specest/ft_specest_mtmconvol.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_specest_mtmconvol", *args, **kwargs)
