from spm.__wrapper__ import Runtime


def bf_inverse_lcmv_multicov(*args, **kwargs):
    """
      Computes LCMV filters using spm_pca_order to constrain inverse of data  
        cov matrix.  
          
        Based on the paper:  
        MEG beamforming using Bayesian PCA for adaptive data covariance matrix regularization.  
        Woolrich M, Hunt L, Groves A, Barnes G.  
        Neuroimage. 2011 Aug 15;57(4)  
          
        and allowing for multiple covariance matrices, e.g. associated with  
        multiple states:  
        Dynamic State Allocation for MEG Source Reconstruction  
        Neuroimage. Woolrich et al. 2013.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_inverse_lcmv_multicov.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_inverse_lcmv_multicov", *args, **kwargs)
