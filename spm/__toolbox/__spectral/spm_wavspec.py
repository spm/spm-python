from spm.__wrapper__ import Runtime


def spm_wavspec(*args, **kwargs):
    """
      Wavelet based spectrogram  
        FORMAT [p] = spm_wavspec (x,freqs,fs,show,rtf)  
        x         Data vector  
        freqs     Frequencies to estimate power at  
        fs        sample rate  
        show      1 to plot real part of wavelet basis used (default = 0)  
        rtf       Wavelet factor (if > 10, then this parameter defaults to a   
                  fixed window length of rtf milliseconds)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/spectral/spm_wavspec.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_wavspec", *args, **kwargs)
