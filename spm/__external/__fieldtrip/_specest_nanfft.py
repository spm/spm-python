from spm.__wrapper__ import Runtime


def _specest_nanfft(*args, **kwargs):
    """
      SPECEST_NANFFT computes a fast Fourier transform in the presence of NaNs  
        in the data  
         
        Use as  
          [spectrum] = specest_nanfft(dat, ...)  
        where  
          dat      = matrix of chan*sample  
          time     = vector, containing time in seconds for each sample  
          spectrum = matrix of taper*chan*foi*toi of fourier coefficients  
         
        Optional arguments should be specified in key-value pairs and can include:  
          basis      = precomputes set of basis functions (sines/cosines)  
          datataype  = 0, 1, 2  
         
        FIXME: FFT speed not yet optimized, e.g. MATLAB version, transpose or not, ...  
        FIXME: function is recursive, should be avoided in favor of transparancy  
         
        See also SPECEST_MTMFFT, SPECEST_CONVOL, SPECEST_HILBERT, SPECEST_MTMCONVOL, SPECEST_MVAR, SPECEST_WAVELET  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/specest_nanfft.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("specest_nanfft", *args, **kwargs)
