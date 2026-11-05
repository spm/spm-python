from spm._runtime import Runtime


def spm_wft(*args, **kwargs):
    r"""
      Windowed fourier wavelet transform (time-frequency analysis)  
        FORMAT [C] = spm_wft(s,k,n)  
        s      - (T X N) time-series  
        k      - Frequencies (cycles per window)  
        n      - window length  
        C      - (w X T X N) coefficients (complex)  
         
        see also: spm_iwft  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_wft.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_wft", *args, **kwargs)
