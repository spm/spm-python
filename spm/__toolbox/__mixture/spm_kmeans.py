from spm.__wrapper__ import Runtime


def spm_kmeans(*args, **kwargs):
    """
      K-means clustering  
        FORMAT [priors,means,covs,post] = spm_kmeans (y,k,method,return_cov)  
         
        y             [N x d] data matrix containing N samples of d-dim data  
        k             number of clusters  
        method        'uniform', 'points' or 'random' (default) seeding  
        return_cov    Set to 1 to return class covariances. Zero otherwise.  
                      (default is 1).  
         
        priors        [1 x k] vector of class prior probabilities  
        means         [k x d] matrix of class means  
        covs          [d x d x k] matrix containing class covariances. This  
                      matrix is empty if return_covs=0  
        post          [N x k] matrix of class labels  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mixture/spm_kmeans.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_kmeans", *args, **kwargs)
