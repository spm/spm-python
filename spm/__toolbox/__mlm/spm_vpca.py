from spm.__wrapper__ import Runtime


def spm_vpca(*args, **kwargs):
    """
      Variational Principal Component Analysis   
        FORMAT [pca] = spm_vpca (T,q,Bayes)  
         
        T     [d x N] matrix containing N d-dimensional data vectors  
              The nth data sample, t_n, is nth column of T  
        q     maximum latent space dimension (q < d)  
        Bayes 1 for Bayesian algorithm, 0 otherwise (default = 1)  
         
        pca model is  
         
              t_n = W x_n + mu + e  
         
        See C. Bishop. Variational Principal Components, ANN, 1999.  
         
        The factor matrix W is a [d x q] matrix, where q=d-1  
        The ith factor is in ith column  
         
        pca  Contains fields for  
         
              ML solution: ml.W, ml.lambda (factor matrix and eigenvalues)  
              Latent variables: M_x, Sigma_x  
              Mean: mean_mu, Sigma_mu  
              Factor Matrix: M_w, Sigma_w   
              Predicted Data: That, mse (mean square error of predictions)  
              Neg Free Energy: Fm, Fm_evol  
              Observation noise precision: mean_tau  
              Prior precisions of Factor magnitudes: mean_alpha  
              Prior precision of Mean: mean_beta  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mlm/spm_vpca.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_vpca", *args, **kwargs)
