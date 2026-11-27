from spm._runtime import Runtime


def spm_vpca_init(*args, **kwargs):
    r"""
      Initialise VPCA model  
        function [W_ml,lambda,sigma2] = spm_vpca_init (T, form_cov)  
         
        T         [d x N] matrix containing N d-dimensional data vectors  
                  The nth data sample, t_n, is nth column of T  
         
        form_cov  form covariance matrix (1=yes, 0=no, default=no)  
          
        W_ml      Maximum Likelihood (ML) estimate of factor matrix  
        lambda    eigenvalues  
        sigma2    Observation noise variance  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mlm/spm_vpca_init.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_vpca_init", *args, **kwargs)
