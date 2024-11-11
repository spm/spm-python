from spm.__wrapper__ import Runtime


def spm_sparse_regression(*args, **kwargs):
    """
      Sparse (logistic) regression using Bayesian model reduction  
        FORMAT RCM = spm_sparse_regression(y,X,X0)  
        y   - univariate response variable  
        X   - design matrix of explanatory variables  
        X0  - confounds  
          
        RCM - reduced causal model structure  
          RCM.M      - GLM  
          RCM.Pp     - Model posterior (with and without each parameter)  
          RCM.Ep     - Bayesian parameter mean under reduced model  
          RCM.Cp     - Bayesian parameter covariance under reduced model  
          RCM.Vp     - Bayesian parameter variance under selected model  
       __________________________________________________________________________  
         
        spm_sparse_regression performs a sparse regression using priors on the  
        parameters of a GLM and hyperpriors on the noise precision to recover a  
        sparse set of explanatory variables. The implicit Bayesian model  
        reduction (i.e., elimination of redundant parameters) uses post-hoc  
        optimisation. If the response variable is in the range [0 1] then a logit  
        transform is applied to produce sparse logistic regression.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_sparse_regression.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_sparse_regression", *args, **kwargs)
