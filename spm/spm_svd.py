from spm._runtime import Runtime


def spm_svd(*args, **kwargs):
    r"""
      Computationally efficient SVD (that can handle sparse arguments)  
        FORMAT [U,S,V] = spm_svd(X,u)  
        X    - (m x n) matrix  
        u    - threshold (1 > u > 0) for normalized eigenvalues (default = 1e-6)  
             - a value of zero induces u = 64*eps  
         
        U    - {m x p} singular vectors  
        V    - {m x p} singular variates  
        S    - {p x p} singular values  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_svd.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_svd", *args, **kwargs)
