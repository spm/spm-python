from spm.__wrapper__ import Runtime


def spm_rar(*args, **kwargs):
    """
      Bayesian autoregressive modelling with zero-mean Gaussian mixture noise  
        function [rar,yclean] = spm_rar (Z,p,m,verbose)  
         
        Z          [N x 1] vector of data points  
        p          Number of AR coefficients  
        m          Number of mixture components (default=2)  
        verbose    0/1 to printout inner workings (default=0)  
         
        rar        Returned model   
        yclean     'Clean' data (ie. with outlier errors removed)  
         
        -------------------------------------------------------  
        The fields in rar are:  
         
        p                The number of AR coefficients  
        m                The number of components  
        fm               The negative free energy  
         
                         In the field priors:  
        lambda_0         Dirichlet parameters for mixing coeffs  
        b_0,c_0          Gamma parameters for precisions  
         
                         In the field posts:  
        lambda           Dirichlet parameters  for mixing coeffs  
        b,c              Gamma parameters for precisions  
        a_mean           AR parameters (posterior mean)  
        a_cov            AR parameters (posterior cov)  
        b_alpha,c_alpha  Gamma parameters for weight precisions  
         
                         Mean posterior values:  
        pi               mixing coefficients (lambda/sum(lambda))  
        variances        variances (1./(b.*c))  
         
        gamma            the responsibilities of each noise component  
         
        For details of algorithm see:  
         
        S.J. Roberts and W.D. Penny. Variational Bayes for Generalised Autoregressive   
        models. IEEE Transactions on Signal Processing, 50(9):2245-2257, 2002  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/spectral/spm_rar.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_rar", *args, **kwargs)
