from spm.__wrapper__ import Runtime


def spm_morlet_conv(*args, **kwargs):
    """
      Temporal convolution of complex spectral responses with Morlet envelope  
        FORMAT [G] = spm_morlet_conv(G,w,dt,wnum)  
         
        G      - (t x w x n x n) cross spectral density  
        w      - Frequencies (Hz)  
        dt     - sampling interval (sec)  
        wnum   - Wavelet number: default = 2  s.d. = wnum/(2*pi*w)  
         
        G      - convolved cross spectral density  
       __________________________________________________________________________  
         
        This routine simply smooths a cross spectral response to emulate a   
        wavelet transform.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_morlet_conv.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_morlet_conv", *args, **kwargs)
