from spm.__wrapper__ import Runtime


def ft_specest_wavelet(*args, **kwargs):
    """
      FT_SPECEST_WAVELET performs time-frequency analysis on any time series trial data  
        using the 'wavelet method' based on Morlet wavelets, doing convolution in the time  
        domain by multiplication in the frequency domain.  
         
        Use as  
          [spectrum, freqoi, timeoi] = ft_specest_wavelet(dat, time, ...)  
        where the input arguments are  
          dat       = matrix of chan*sample  
          time      = vector, containing time in seconds for each sample  
        and the output arguments are  
          spectrum  = array of chan*freqoi*timeoi of fourier coefficients  
          freqoi    = vector of frequencies in spectrum  
          timeoi    = vector of timebins in spectrum  
         
        Optional arguments should be specified in key-value pairs and can include  
          timeoi    = vector, containing time points of interest (in seconds)  
          freqoi    = vector, containing frequencies of interest  
          width     = number or vector, width of the wavelet, determines the temporal and spectral resolution  
          gwidth    = number, determines the length of the used wavelets in standard deviations of the implicit Gaussian kernel  
          pad       = number, total length of data after zero padding (in seconds)  
          padtype   = string, indicating type of padding to be used, can be 'zero', 'mean', 'localmean', 'edge', or 'mirror' (default = 'zero')  
          polyorder = number, the order of the polynomial to fitted to and removed from the data prior to the fourier transform (default = 0 -> remove DC-component)  
          verbose   = output progress to console (0 or 1, default 1)  
         
        See also FT_FREQANALYSIS, FT_SPECEST_MTMCONVOL, FT_SPECEST_TFR, FT_SPECEST_HILBERT, FT_SPECEST_MTMFFT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/specest/ft_specest_wavelet.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_specest_wavelet", *args, **kwargs)
