from spm.__wrapper__ import Runtime


def spm_mtf2ccf(*args, **kwargs):
    """
      Converts modulation transfer function to cross covariance function  
        FORMAT [ccf,pst] = spm_mtf2ccf(mtf,Hz)  
         
        mtf  (N,n,n)   - (unnormalised) directed or modulation transfer function  
        Hz   (N x 1)   - vector of frequencies (Hz)  
         
        ccf  (M,:,:)   - cross covariance functions  
        pst  (M,1)     - vector of lags for evaluation (seconds)  
         
        See also:   
         spm_ccf2csd.m, spm_ccf2mar, spm_csd2ccf.m, spm_csd2mar.m, spm_mar2csd.m,  
         spm_csd2coh.m, spm_Q.m, spm_mar.m and spm_mar_spectral.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/spectral/spm_mtf2ccf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mtf2ccf", *args, **kwargs)
