from spm.__wrapper__ import Runtime


def spm_normrnd(*args, **kwargs):
    """
      Random samples from Gaussian distribution   
        FORMAT x = spm_normrnd(m, C, N)  
        m        - [d x 1] mean  
        C        - [d x d] covariance or cell array {dC, vC} so that  
                   [vC, diag(dC)] = eig(C)  
        N        - number of samples  
         
        x        - [d x N] matrix of samples  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_normrnd.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_normrnd", *args, **kwargs)
