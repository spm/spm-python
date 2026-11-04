from spm._runtime import Runtime


def spm_normrnd(*args, **kwargs):
    r"""
      Random samples from Gaussian distribution   
        FORMAT x = spm_normrnd(m, C, N)  
        m        - [d x 1] mean  
        C        - [d x d] covariance or cell array {dC, vC} so that  
                   [vC, diag(dC)] = eig(C)  
        N        - number of samples  
         
        x        - [d x N] matrix of samples  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_normrnd.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_normrnd", *args, **kwargs)
