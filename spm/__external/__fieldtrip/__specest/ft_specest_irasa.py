from spm.__wrapper__ import Runtime


def ft_specest_irasa(*args, **kwargs):
    """
      FT_SPECEST_IRASA separates the fractal components from the orginal power spectrum  
        using Irregular-Resampling Auto-Spectral Analysis (IRASA)  
         
        Use as  
          [spectrum, ntaper, freqoi] = ft_specest_irasa(dat, time, ...)  
        where the input arguments are  
          dat        = matrix of chan*sample  
          time       = vector, containing time in seconds for each sample  
        and the output arguments are  
          spectrum   = matrix of taper*chan*freqoi of fourier coefficients  
          ntaper     = vector containing number of tapers per element of freqoi  
          freqoi     = vector of frequencies in spectrum  
         
        Optional arguments should be specified in key-value pairs and can include  
          freqoi     = vector, containing frequencies of interest  
          output     = string, indicating type of output ('fractal' or 'original', default 'fractal')  
          pad        = number, total length of data after zero padding (in seconds)  
          padtype    = string, indicating type of padding to be used, can be 'zero', 'mean', 'localmean', 'edge', or 'mirror' (default = 'zero')  
          polyorder  = number, the order of the polynomial to fitted to and removed from the data prior to the Fourier transform (default = 0, which removes the DC-component)  
          verbose    = boolean, output progress to console (0 or 1, default 1)  
         
        This implements: Wen.H. & Liu.Z.(2016), Separating fractal and oscillatory components in the power  
        spectrum of neurophysiological signal. Brain Topogr. 29(1):13-26. The source code accompanying the  
        original paper is avaible from https://purr.purdue.edu/publications/1987/1  
         
        For more information about the difference between the current and previous version and how to use this  
        function, please see https://www.fieldtriptoolbox.org/example/irasa/  
         
        See also FT_FREQANALYSIS, FT_SPECEST_MTMFFT, FT_SPECEST_MTMCONVOL, FT_SPECEST_TFR, FT_SPECEST_HILBERT, FT_SPECEST_WAVELET  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/specest/ft_specest_irasa.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_specest_irasa", *args, **kwargs)
