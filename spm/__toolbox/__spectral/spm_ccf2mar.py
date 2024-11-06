from spm.__wrapper__ import Runtime


def spm_ccf2mar(*args, **kwargs):
    """
      Converts cross covariance function to cross spectral density  
        FORMAT [mar] = spm_ccf2mar(ccf,p)  
         
        ccf  (N,m,m)   - cross covariance functions  
        p              - AR(p) order [default: p = 8]  
         
        mar.noise_cov  - (m,m)         covariance of innovations     
        mar.mean       - (p*m,m)       MAR coeficients (matrix format - positive)  
        mar.lag        - lag(p).a(m,m) MAR coeficients (array format  - negative)  
        mar.p          - order of a AR(p) model  
         
        See also:  
         spm_ccf2csd.m, spm_ccf2mar, spm_csd2ccf.m, spm_csd2mar.m, spm_mar2csd.m,  
         spm_csd2coh.m, spm_dcm_mtf.m, spm_Q.m, spm_mar.m and spm_mar_spectral.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/spectral/spm_ccf2mar.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ccf2mar", *args, **kwargs)
