from spm.__wrapper__ import Runtime


def spm_csd(*args, **kwargs):
    """
      Cross spectral density using Welch's method  
        FORMAT [csd,Hz] = spm_csd(Y,Hz,ns)  
         
        Y    (:,m)            - data  
        Hz   (n x 1)          - vector of frequencies (Hz)  
        ns                    - sampling frequency (default = 2*Hz(end))  
        psd                   - 1 for power spectral density [default = 0]  
         
        csd  (n,:,:)          - cross spectral density (cf, mar.P)  
         
        See: cpsd.m and  
         spm_ccf2csd.m, spm_ccf2mar, spm_csd2ccf.m, spm_csd2mar.m, spm_mar2csd.m,  
         spm_csd2coh.m, spm_Q.m, spm_mar.m and spm_mar_spectral.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/spectral/spm_csd.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_csd", *args, **kwargs)
