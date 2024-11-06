from spm.__wrapper__ import Runtime


def spm_mar2ccf(*args, **kwargs):
    """
      Get the cross covariance function from MAR coefficients or structure  
        FORMAT [ccf] = spm_mar2ccf(mar,n)  
         
        mar   - MAR coefficients or structure (see spm_mar.m)  
        n     - number of time bins [default: n = 128]  
         
        ccf   - (2*n + 1,i,j) cross covariance functions between I and J  
         
        The mar coefficients are either specified in a cell array (as per  
        spm_mar) or as a vector of (positive) coefficients as per spm_Q. The  
        former are the negative values of the latter. If mar is a matrix of size  
        d*p x d - it is assumed that the (positive) coefficients  run fast over   
        lag = p, as per the DCM routines.  
         
        see also:  
         spm_ccf2csd.m, spm_ccf2mar, spm_csd2ccf.m, spm_csd2mar.m, spm_mar2csd.m,  
         spm_csd2coh.m, spm_Q.m, spm_mar.m and spm_mar_spectral.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/spectral/spm_mar2ccf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mar2ccf", *args, **kwargs)
