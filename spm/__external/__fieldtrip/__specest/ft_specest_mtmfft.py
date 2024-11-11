from spm.__wrapper__ import Runtime


def ft_specest_mtmfft(*args, **kwargs):
    """
      FT_SPECEST_MTMFFT computes a fast Fourier transform using multitapering with  
        multiple tapers from the DPSS sequence or using a variety of single tapers.  
         
        Use as  
          [spectrum, ntaper, freqoi] = ft_specest_mtmfft(dat, time, ...)  
        where the input arguments are  
          dat        = matrix of chan*sample  
          time       = vector, containing time in seconds for each sample  
        and the output arguments are  
          spectrum   = matrix of ntaper*nchan*nfreq of fourier coefficients  
          ntaper     = vector containing number of tapers per element of freqoi  
          freqoi     = vector of frequencies in spectrum  
         
        Optional arguments should be specified in key-value pairs and can include  
          freqoi     = vector, containing frequencies of interest  
          taper      = 'dpss', 'hanning' or many others, see WINDOW (default = 'dpss')  
          taperopt   = additional taper options to be used in the WINDOW function, see WINDOW  
          tapsmofrq  = the amount of spectral smoothing through multi-tapering. Note: 4 Hz smoothing means plus-minus 4 Hz, i.e. a 8 Hz smoothing box  
          pad        = number, total length of data after zero padding (in seconds)  
          padtype    = string, indicating type of padding to be used, can be 'zero', 'mean', 'localmean', 'edge', or 'mirror' (default = 'zero')  
          dimord     = 'tap_chan_freq' (default) or 'chan_time_freqtap' for memory efficiency (only when using variable number of slepian tapers)  
          polyorder  = number, the order of the polynomial to fitted to and removed from the data prior to the fourier transform (default = 0 -> remove DC-component)  
          verbose    = output progress to console (0 or 1, default 1)  
         
        See also FT_FREQANALYSIS, FT_SPECEST_MTMCONVOL, FT_SPECEST_TFR, FT_SPECEST_HILBERT, FT_SPECEST_WAVELET  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/specest/ft_specest_mtmfft.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_specest_mtmfft", *args, **kwargs)
