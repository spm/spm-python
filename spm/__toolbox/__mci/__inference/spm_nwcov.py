from spm.__wrapper__ import Runtime


def spm_nwcov(*args, **kwargs):
    """
      Get second moments of Normal-Wishart  
        FORMAT [M] = spm_nwcov (M)  
         
        .mean_prior_cov    Prior covariance of mean  
        .sample_prior_cov  Prior covariance of samples  
        .mean_post_cov     Posterior covariance of mean  
        .sample_pred_cov   Predictive covariance of samples  
         
        The latter quantity is also the covariance of the predictive density  
        The marginal distributions of the mean and of the samples   
        are multivariate-T, not Gaussian.  
         
        See J. Bernardo and A. Smith (2000)   
        Bayesian Theory, Wiley (page 435)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_nwcov.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_nwcov", *args, **kwargs)
