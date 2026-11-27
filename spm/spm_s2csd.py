from spm._runtime import Runtime


def spm_s2csd(*args, **kwargs):
    r"""
      Convert eigenspectrum to cross spectral density  
        FORMAT [csd,Hz] = spm_s2csd(s,Hz)  
         
        s    (m x 1}        - eigenspectrum  
        Hz   (n x 1)        - vector of frequencies (Hz)  
         
        csd  (n,m)          - spectral density (of modes)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_s2csd.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_s2csd", *args, **kwargs)
