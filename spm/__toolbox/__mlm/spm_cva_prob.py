from spm.__wrapper__ import Runtime


def spm_cva_prob(*args, **kwargs):
    """
      Probabilistic Canonical Variates Analysis  
        FORMAT [CVA] = spm_cva_prob (X1,X2,m)  
         
        X1           [d1 x N] matrix of dependent variables  
        X2           [d2 x N] matrix of independent variables  
        m            dimension of latent variable (min([d1,d2]) by default)  
         
        Returns fields:  
          
        .U1,.U2      Canonical vectors  
        .W1,.W2      Factor matrices  
        .L           Log-Likelihood  
        .bic         Bayesian Information Criterion  
        .aic         Akaike's Information Criterion  
         
        Fits probabilistic model  
         
        x1 = W1 z + e1  
        x2 = W2 z + e2  
         
        This algorithm is described in:  
         
        F. Bach and M. Jordan (2005) A probabilistic interpretation of canonical  
        correlation analysis. Dept. Stats, Univ California, Berkeley CA.   
        Tech Rep 688.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mlm/spm_cva_prob.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_cva_prob", *args, **kwargs)
