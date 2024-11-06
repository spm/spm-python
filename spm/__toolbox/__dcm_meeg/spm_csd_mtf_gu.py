from spm.__wrapper__ import Runtime


def spm_csd_mtf_gu(*args, **kwargs):
    """
      Spectral desnities of innovations and noise for DCM for CSD  
        FORMAT [Gu,Gs,Gn,f] = spm_csd_mtf_gu(P,M)  
        FORMAT [Gu,Gs,Gn,f] = spm_csd_mtf_gu(P,f)  
         
        P   - parameters  
        M   - neural mass model structure (with M.Hz)  
        f   - frequencies of interest (Hz)  
         
        Gu  - neuronal innovations  
        Gn  - channel noise (non-specific)  
        Gs  - channel noise (specific)  
         
        f   - frequency  
         
        fluctuations and noise parameters: for n regions and c channels  
       --------------------------------------------------------------------------  
           pE.a(2,n) - neuronal fluctuations        - amplitude and exponent  
           pE.b(2,c) - channel noise (non-specific) - amplitude and exponent  
           pE.c(2,c) - channel noise (specific)     - amplitude and exponent  
           pE.d(8,n) - neuronal fluctuations        - basis set coefficients  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_csd_mtf_gu.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_csd_mtf_gu", *args, **kwargs)
