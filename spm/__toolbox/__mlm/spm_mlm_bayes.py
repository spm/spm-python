from spm.__wrapper__ import Runtime


def spm_mlm_bayes(*args, **kwargs):
    """
      Bayesian Multivariate Linear Modelling  
        FORMAT [mlm] = spm_mlm_bayes (y,x,pr,verbose,ml_only)  
         
        MLM: y = x W + e  
         
        y           T-by-d data matrix   
        x           N-by-p design matrix  
        pr          Shrinkage prior on MLM coefficients:  
                    'input' (default), 'output' or 'global'  
         
                    For 'input', coeffs of each independent variable  
                    ie rows of W, share same prior precision. This   
                    allows some inputs to be more relevant than others.  
         
                    For 'output', cols of W share same prior precision.  
                    This allows some outputs to be more relevant.  
         
                    For 'global' there is a single prior precision.  
         
        verbose     1 to print out iteration details, 0 otherwise (default=0)  
        ml_only     set to 1 to only compute ML solution. Default is zero  
         
        The returned data structure mlm contains the following fields  
         
        .wmean      Bayes estimate of [p x d] regression coefficient matrix  
        .wsd        [p x d] posterior standard deviations of reg coeffs  
        .wml        Maximum Likelihood regression coefficient matrix  
        .wcov       [pd x pd] posterior covariance of regression coeffs  
        .lambda     [d x d] observation noise precision matrix  
        .fm         Negative free energy of model  
        .bic        Bayesian Information Criterion  
        .iterations Number of iterations during optimisation  
        .prior      Details of regression coeff prior  
                    .group(j).mean_alpha:  
                    Estimated prior precision of jth parameter group.  
                    For 'input' prior this is jth row of W.   
                    For 'output' prior this is jth column of W.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mlm/spm_mlm_bayes.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mlm_bayes", *args, **kwargs)
