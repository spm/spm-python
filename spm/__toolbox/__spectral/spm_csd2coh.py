from spm._runtime import Runtime


def spm_csd2coh(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/spectral/spm_csd2coh.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_csd2coh", *args, **kwargs)
