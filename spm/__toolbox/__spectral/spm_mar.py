from spm.__wrapper__ import Runtime


def spm_mar(*args, **kwargs):
    """
      Bayesian Multivariate Autoregressive Modelling  
        FORMAT [mar,y,y_pred] = spm_mar (X,p,prior,verbose)  
         
        Matrix of AR coefficients are in form  
        x_t = -a_1 x_t-1 - a_2 x_t-2 + ...... - a_p x_t-p  
        where a_k is a d-by-d matrix of coefficients at lag k and x_t-k's are   
        vectors of a d-variate time series.  
         
        X              T-by-d matrix containing d-variate time series  
        p              Order of MAR model  
        prior          Prior on MAR coefficients (see marprior.m)  
        verbose        1 to print out iteration details, 0 otherwise (default=0)  
         
        mar.lag(k).a   AR coefficient matrix at lag k  
        mar.noise_cov  Estimated noise covariance  
        mar.fm         Free energy of model  
        mar.wmean      MAR coefficients stored in a matrix  
        y              Target values  
        y_pred         Predicted values  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/spectral/spm_mar.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mar", *args, **kwargs)
