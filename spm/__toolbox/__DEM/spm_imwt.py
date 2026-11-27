from spm._runtime import Runtime


def spm_imwt(*args, **kwargs):
    r"""
      Inverse windowed Fourier transform - continuous synthesis  
        FORMAT [s] = spm_imwt(C,k,w);  
        s      - 1-D time-series  
        k      - Frequencies (cycles per window)  
        w      - window length  
        C      - coefficients (complex)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_imwt.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_imwt", *args, **kwargs)
