from spm.__wrapper__ import Runtime


def spm_mar2gew(*args, **kwargs):
    """
      Get spectral estimates from MAR model  
        FORMAT [gew,pve] = spm_mar2gew(mar,Hz,ns)  
         
        mar   - MAR coefficients or structure (see spm_mar.m)  
        Hz    - [N x 1] vector of frequencies to evaluate spectra at  
        ns    - samples per second [default: ns = 2*Hz(end)]  
         
        gwe  (N,m,m)   - Geweke's frequency domain Granger causality  
        pve  (N,m,m)   - proportion of variance explained  
         
        The mar coefficients are either specified in a cell array (as per  
        spm_mar) or as a vector of (positive) coefficients as per spm_Q. The  
        former are the negative values of the latter. If mar is a matrix of size  
        d*p x d - it is assumed that the (positive) coefficients  run fast over   
        lag = p, as per the DCM routines.  
         
        See also: spm_???2???.m  
            ??? = {'ccf','csd','gew','mar','coh','mtf','ker','ssm','dcm'}  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/spectral/spm_mar2gew.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mar2gew", *args, **kwargs)
