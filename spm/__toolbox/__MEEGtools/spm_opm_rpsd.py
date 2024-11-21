from spm.__wrapper__ import Runtime


def spm_opm_rpsd(*args, **kwargs):
    """
      Compute relative PSD of two OPM datasets (for checking shielding factors)  
        FORMAT D = spm_opm_rpsd(S)  
          S               - input structure  
         fields of S:  
          S.D1            - SPM MEEG object                      - Default: no Default  
          S.D2            - SPM MEEG object                      - Default: no Default  
          S.triallength   - window size (ms)                      - Default: 1000  
          S.bc            - boolean to dc correct                 - Default: 0  
          S.channels      - channels to estimate PSD from         - Default: 'ALL'  
          S.dB            - boolean to return decibels            - Default: 0  
          S.plot          - boolean to plot or not                - Default: 0  
        Output:  
          sf              - Shielding factor ( in data units or decibels)  
          f               - frequencies psd is sampled at  
       __________________________________________________________________________  
        Copyright (C) 2018-2022 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_opm_rpsd.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_opm_rpsd", *args, **kwargs)
