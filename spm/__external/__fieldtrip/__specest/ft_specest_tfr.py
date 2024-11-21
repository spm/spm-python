from spm.__wrapper__ import Runtime


def ft_specest_tfr(*args, **kwargs):
    """
      FT_SPECEST_TFR performs time-frequency analysis on any time series trial data using  
        the 'wavelet method' based on Morlet wavelets, doing convolution in the time  
        domain.  
         
        Use as  
          [spectrum, freqoi, timeoi] = ft_specest_convol(dat, time, ...)  
        where the input arguments are  
          dat       = matrix of nchan*nsample  
          time      = vector, containing time in seconds for each sample  
        and the output arguments are  
          spectrum  = array of nchan*nfreq*ntime of fourier coefficients  
          freqoi    = vector of frequencies in spectrum  
          timeoi    = vector of timebins in spectrum  
         
        Optional arguments should be specified in key-value pairs and can include  
          timeoi    = vector, containing time points of interest (in seconds, analysis window will be centered around these time points)  
          freqoi    = vector, containing frequencies (in Hz)  
          width     = number or vector, width of the wavelet, determines the temporal and spectral resolution (default = 7)  
          gwidth    = number, determines the length of the used wavelets in standard deviations of the implicit Gaussian kernel  
          polyorder = number, the order of the polynomial to fitted to and removed from the data prior to the fourier transform (default = 0 -> remove DC-component)  
          verbose   = output progress to console (0 or 1, default 1)  
         
        See also FT_FREQANALYSIS, FT_SPECEST_MTMFFT, FT_SPECEST_MTMCONVOL, FT_SPECEST_HILBERT, FT_SPECEST_NANFFT, FT_SPECEST_WAVELET  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/specest/ft_specest_tfr.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_specest_tfr", *args, **kwargs)
