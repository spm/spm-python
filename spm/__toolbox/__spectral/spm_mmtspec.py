from spm.__wrapper__ import Runtime


def spm_mmtspec(*args, **kwargs):
    """
      Moving multitaper based spectrogram  
        FORMAT [p, f, t] = spm_mmtspec (x,Fs,freqs,timeres)  
         
        x         input time series  
        Fs        sampling frequency of input time series  
        freqs     desired vector of frequencies for spectrogram eg. [6:1:30]  
        timeres   desired time resolution for spectrogram, default T/16  
                  where T is duration of x  
         
        p         p(f, t) is estimate of power at freq f and time t  
          
        Time series is split into a series of overlapping windows with 5% overlap.   
        Desired frequency resolution is attained by zero padding   
        as/if necessary. The taper approach is applied to each padded sample.  
          
        Plot spectrogram using imagesc(t,f,p); axis xy  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/spectral/spm_mmtspec.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mmtspec", *args, **kwargs)
