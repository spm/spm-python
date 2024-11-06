from spm.__wrapper__ import Runtime


def spm_csd2gew(*args, **kwargs):
    """
      Convert cross sspectral density to Geweke Granger causality  
        FORMAT [gew,pve,H] = spm_csd2gew(csd,Hz,u)  
         
        ccf  (N,m,m)   - cross covariance functions  
        Hz   (n x 1)   - vector of frequencies (Hz)  
        u    (1)       - regularizer (default: 1);  
         
        gwe  (N,m,m)   - Geweke's frequency domain Granger causality  
        pve  (N,m,m)   - proportion of variance explained  
        H    (N,m,m)   - transfer function matrix  
         
        This routine uses the Wilson-Burg algorithm to perform spectral matrix  
        factorisation. The minimum phase factor is then used to form the noise  
        covariance (covariance of the innovations) and implicitly derive the  
        transfer functions (and spectral Granger causality).  
         
        See also:  
         spm_ccf2csd.m, spm_ccf2mar, spm_csd2ccf.m, spm_csd2mar.m, spm_mar2csd.m,  
         spm_csd2coh.m, spm_dcm_mtf.m, spm_Q.m, spm_mar.m and spm_mar_spectral.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/spectral/spm_csd2gew.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_csd2gew", *args, **kwargs)
