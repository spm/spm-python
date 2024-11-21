from spm.__wrapper__ import Runtime


def spm_csd2coh(*args, **kwargs):
    """
      Converts cross spectral density to coherence and (phase) delay  
        FORMAT [coh,fsd] = spm_csd2coh(csd,Hz)  
         
        csd  (Hz,:,:) - cross spectral density (cf, mar.P)  
        Hz   (n x 1)  - vector of frequencies  
         
        coh           - coherence  
        fsd           - frequency specific delay (seconds)   
                      - phase-delay/radial frequency  
         
        See also: spm_???2???.m  
            ??? = {'ccf','csd','gew','mar','coh','mtf','ker','ssm','dcm'}  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/spectral/spm_csd2coh.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_csd2coh", *args, **kwargs)
