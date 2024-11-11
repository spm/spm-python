from spm.__wrapper__ import Runtime


def ft_specest_neuvar(*args, **kwargs):
    """
      FT_SPECEST_NEUVAR computes a time-domain estimation of overall signal power, having  
        compensated for the 1/f distribution of spectral content.  
         
        Use as  
          [spectrum, freqoi] = ft_specest_neuvar(dat, time...)  
        where the input arguments are  
          dat        = matrix of chan*sample  
          time       = vector, containing time in seconds for each sample  
        and the output arguments are  
          spectrum   = matrix of chan*neuvar  
          freqoi     = vector of frequencies in spectrum  
         
        Optional arguments should be specified in key-value pairs and can include  
          order      = number, the order of differentation for compensating for the 1/f (default = 1)  
          pad        = number, total length of data after zero padding (in seconds)  
          padtype    = string, indicating type of padding to be used, can be 'zero', 'mean', 'localmean', 'edge', or 'mirror' (default = 'zero')  
          polyorder  = number, the order of the polynomial to fitted to and removed from the data prior to the Fourier transform (default = 0, which removes the DC-component)  
          verbose    = output progress to console (0 or 1, default 1)  
         
        See also FT_FREQANALYSIS, FT_SPECEST_MTMFFT, FT_SPECEST_MTMCONVOL, FT_SPECEST_TFR, FT_SPECEST_HILBERT, FT_SPECEST_WAVELET  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/specest/ft_specest_neuvar.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_specest_neuvar", *args, **kwargs)
