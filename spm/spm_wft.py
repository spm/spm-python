from spm.__wrapper__ import Runtime


def spm_wft(*args, **kwargs):
    """
      Windowed fourier wavelet transform (time-frequency analysis)  
        FORMAT [C] = spm_wft(s,k,n)  
        s      - (t X n) time-series  
        k      - Frequencies (cycles per window)  
        n      - window length  
        C      - (w X t X n) coefficients (complex)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_wft.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_wft", *args, **kwargs)
