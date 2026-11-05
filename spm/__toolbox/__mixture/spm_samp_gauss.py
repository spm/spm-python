from spm._runtime import Runtime


def spm_samp_gauss(*args, **kwargs):
    r"""
      Sample from a Gaussian PDF  
        FORMAT [x] = spm_samp_gauss (m, C, N, dC, vC)  
        m     [d x 1] mean  
        C     [d x d] covar  
        N     Number of samples  
        dC    diagonalised C [d x 1]  
        vC    eigenvectors of C [d x d]  
         
        x     [N x d] matrix of samples  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mixture/spm_samp_gauss.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_samp_gauss", *args, **kwargs)
