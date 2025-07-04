from spm._runtime import Runtime


def spm_dtf2gew(*args, **kwargs):
    """
      Converts directed transfer function to Geweke Granger causality  
        FORMAT [gew,pve] = spm_csd2gew(dtf,C)  
         
        dtf  (N,n,n)   - (unnormalised) directed or modulation transfer function  
        C              - optional noise (fluctation) covariance matrix C(n,n)  
                       - or cross spectral density C(N,n,n)  
                       - or spectral power C(N,n)  
         
        gew  (N,n,n)   - Geweke's frequency domain Granger causality  
        pve  (N,n,n)   - proportion of variance explained  
         
        See also:  
         spm_ccf2csd.m, spm_ccf2mar, spm_csd2ccf.m, spm_csd2mar.m, spm_mar2csd.m,  
         spm_csd2coh.m, spm_dcm_mtf.m, spm_Q.m, spm_mar.m and spm_mar_spectral.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/spectral/spm_dtf2gew.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dtf2gew", *args, **kwargs)
