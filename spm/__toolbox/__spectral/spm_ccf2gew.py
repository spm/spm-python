from spm.__wrapper__ import Runtime


def spm_ccf2gew(*args, **kwargs):
    """
      Converts cross covariance function to Geweke Granger causality  
        FORMAT [gew] = spm_ccf2gew(ccf,Hz,dt,p)  
         
        ccf  (N,m,m)   - cross covariance functions  
        Hz   (n x 1)   - vector of frequencies (Hz)  
        dt             - samping interval [default dt = 1/(2*Hz(end))]  
        p              - AR(p) order [default p = 8]  
         
        gwe   (N,m,m)  - Geweke's frequency domain Granger causality  
         
        See also: spm_???2???.m  
            ??? = {'ccf','csd','gew','mar','coh','mtf','ker','ssm','dcm'}  
        and spm_Q.m, spm_mar.m, spm_mar_spectral.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/spectral/spm_ccf2gew.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ccf2gew", *args, **kwargs)
