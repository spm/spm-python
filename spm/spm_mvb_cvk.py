from spm.__wrapper__ import Runtime


def spm_mvb_cvk(*args, **kwargs):
    """
      K-fold cross validation of a multivariate Bayesian model  
        FORMAT [p_value,percent,R2] = spm_mvb_cvk(MVB,k)  
         
        MVB - Multivariate Bayes structure  
        k   - k-fold cross-validation ('0' implies a leave-one-out scheme)  
         
        p   - p-value: under a null GLM  
        percent: proportion correct (median threshold)  
        R2  - coefficient of determination  
         
        spm_mvb_cvk performs a k-fold cross-validation by trying to predict  
        the target variable using training and test partitions on orthogonal   
        mixtures of data (from null space of confounds)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mvb_cvk.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mvb_cvk", *args, **kwargs)
