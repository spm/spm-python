from spm.__wrapper__ import Runtime


def spm_ancova(*args, **kwargs):
    """
      Estimation and inference of a linear model  
        FORMAT [F,df,beta,xX,xCon] = spm_ancova(xX,V,Y,c);  
         
        xX    - (m x p) Design matrix or structure  
        V     - (m x m) error covariance constraint  
        Y     - {m x n} matrix of response {m x 1} variables  
        c     - {p x q} matrix of (q) contrasts  
         
        F     - {t x n} matrix of T or F values  
        df    - {1 x 2} vector of degrees of freedom  
        beta  - {p x n} matrix of parameter estimates  
        xX    - design matrix structure  
        xCon  - contrast structure  
       __________________________________________________________________________  
         
        spm_ancova uses a General Linear Model of the form:  
         
          Y  = X*beta + K*e  
         
        to compute the parameter estimates (beta) and make inferences (T or F)  
        where V = K*K' represents the correlation structure. If c has only one  
        column T statistics are returned, otherwise F ratios are computed.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_ancova.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ancova", *args, **kwargs)
