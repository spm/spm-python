from spm._runtime import Runtime


def spm_mvb_cvk2(*args, **kwargs):
    """
      k-fold cross validation of a multivariate Bayesian model  
        FORMAT [p_value,percent,R2] = spm_mvb_cvk(MVB,k)  
         
        MVB - Multivariate Bayes structure  
        k   - k-fold cross-validation ('0' implies a leave-one-out scheme)  
         
        p   - p-value: under a null GLM  
        percent: proportion correct (median threshold)  
        R2  - coefficient of determination  
         
        spm_mvb_cvk performs a k-fold cross-validation by trying to predict  
        the target variable using training and test partitions on orthogonal   
        mixtures of data (from null space of confounds).  
        This version uses the optimised covariance model from spm_mvb.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mvb_cvk2.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mvb_cvk2", *args, **kwargs)
