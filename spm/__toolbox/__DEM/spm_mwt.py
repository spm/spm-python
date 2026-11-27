from spm._runtime import Runtime


def spm_mwt(*args, **kwargs):
    r"""
      Morlet wavelet transform (time-frequency analysis)  
        FORMAT [C] = spm_mwt(s,k,w)  
        s      - (T X N) time-series  
        k      - Frequencies (cycles per window)  
        w      - window length  
        C      - (w X T X N) coefficients (complex)  
         
        see also: spm_iwft  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_mwt.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mwt", *args, **kwargs)
