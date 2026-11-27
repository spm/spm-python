from spm._runtime import Runtime


def spm_iwft(*args, **kwargs):
    r"""
      Inverse windowed Fourier transform - continuous synthesis  
        FORMAT [s] = spm_iwft(C,k,n);  
        s      - 1-D time-series  
        k      - Frequencies (cycles per window)  
        n      - window length  
        C      - coefficients (complex)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_iwft.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_iwft", *args, **kwargs)
