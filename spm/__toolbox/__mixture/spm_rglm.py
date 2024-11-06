from spm.__wrapper__ import Runtime


def spm_rglm(*args, **kwargs):
    """
      Fit a Robust GLM   
        FORMAT [rglm,yclean] = spm_rglm (y,X,m,priors,verbose)  
         
        The noise is modelled with a Mixture of Zero-Mean Gaussians   
         
        y          [N x 1] data vector  
        X          [N x p] design matrix  
        m          Number of mixture components  
        priors     .alpha      [1 x 1] weight precision (default=0.001)  
                   .mean_err   [m x 1] vector of mean error SD  
                   .std_err    [m x 1] vector of dev of error SD  
        verbose    0/1 to printout inner workings (default=0)  
         
        rglm       Returned model   
        yclean     'Clean' data  
         
        -------------------------------------------------------  
        The fields in rglm are:  
         
        m                The number of error components  
        fm               The negative free energy  
        loops            Number of iterations used  
         
                         In the field priors:  
         
        lambda_0         Dirichlet parameters for mixing coeffs  
        b_0,c_0          Gamma parameters for precisions  
         
                         In the field posts:  
         
        lambda           Dirichlet parameters  for mixing coeffs  
        b,c              Gamma parameters for precisions  
        w_mean           Mean estimated regression coefficients  
        w_cov            Covariance of regression coefficients  
        pi               mixing coefficients (lambda/sum(lambda))  
        variances        variances (1./(b.*c))  
        gamma            the responsilities of each noise component  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mixture/spm_rglm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_rglm", *args, **kwargs)
