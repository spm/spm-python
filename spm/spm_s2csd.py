from spm.__wrapper__ import Runtime


def spm_s2csd(*args, **kwargs):
    """
      Convert eigenspectrum to cross spectral density  
        FORMAT [csd,Hz] = spm_s2csd(s,Hz)  
         
        s    (m x 1}        - eigenspectrum  
        Hz   (n x 1)        - vector of frequencies (Hz)  
         
        csd  (n,m)          - spectral density (of modes)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_s2csd.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_s2csd", *args, **kwargs)
