from spm.__wrapper__ import Runtime


def spm_Q(*args, **kwargs):
    """
      Return an (n x n) (inverse) autocorrelation matrix for an AR(p) process  
        FORMAT [Q] = spm_Q(a,n,q)  
         
        a  - vector of (p) AR coefficients  
        n  - size of Q  
        q  - switch to return inverse autocorrelation or precision [default q = 0]  
       __________________________________________________________________________  
        spm_Q uses a Yule-Walker device to compute K where:  
          
        y = K*z  
          
        such that y is an AR(p) process generated from an i.i.d innovation   
        z.  This means  
          
        cov(y) = <K*z*z'*K> = K*K'  
          
        If called with q ~= 0, a first order process is assumed when evaluating  
        the precision (inverse covariance) matrix; i.e., a = a(1)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_Q.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_Q", *args, **kwargs)
