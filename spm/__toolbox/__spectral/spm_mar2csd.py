from spm.__wrapper__ import Runtime


def spm_mar2csd(*args, **kwargs):
    """
      Get spectral estimates from MAR model  
        FORMAT [csd,dtf,coh,pha] = spm_mar2csd(mar,Hz,ns)  
         
        mar   - MAR coefficients or structure (see spm_mar.m)  
        Hz    - [Nf x 1] vector of frequencies to evaluate spectra at  
        ns    - samples per second [default: ns = 2*Hz(end)]  
         
        csd   - cross spectral density  
        mtf   - modulation transfer function  
        coh   - coherence  
        pha   - phase  
         
        The mar coefficients are either specified in a cell array (as per  
        spm_mar) or as a vector of (positive) coefficients as per spm_Q. The  
        former are the negative values of the latter. If mar is a matrix of size  
        d*p x d - it is assumed that the (positive) coefficients  run fast over   
        lag = p, as per the DCM routines.  
         
        see also:  
         spm_ccf2csd.m, spm_ccf2mar, spm_csd2ccf.m, spm_csd2mar.m, spm_mar2ccf.m,  
         spm_csd2coh.m, spm_Q.m, spm_mar.m and spm_mar_spectral.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/spectral/spm_mar2csd.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mar2csd", *args, **kwargs)
