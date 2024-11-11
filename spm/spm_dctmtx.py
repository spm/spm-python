from spm.__wrapper__ import Runtime


def spm_dctmtx(*args, **kwargs):
    """
      Create basis functions for Discrete Cosine Transform  
        FORMAT C = spm_dctmtx(N)  
        FORMAT C = spm_dctmtx(N,K)  
        FORMAT C = spm_dctmtx(N,K,n)  
        FORMAT D = spm_dctmtx(N,K,'diff')  
        FORMAT D = spm_dctmtx(N,K,n,'diff')  
        FORMAT D = spm_dctmtx(N,K,'diff',dx)  
         
        N        - dimension  
        K        - order  
        n        - optional points to sample  
         
        C        - DCT matrix or its derivative  
       __________________________________________________________________________  
         
        spm_dctmtx creates a matrix for the first few basis functions of a one  
        dimensional discrete cosine transform.  
        With the 'diff' argument, spm_dctmtx produces the derivatives of the DCT.  
         
        If N and K are vectors, C is a large prod(N) x prod(K) matrix  
        corresponding to the Kronecker tensor product of each N-dimensional  
        basis set. This is useful for dealing with vectorised N-arrays. An  
        additional argument, dx can be specified to scale the derivatives  
         
        Reference:  
        Fundamentals of Digital Image Processing (p 150-154). Anil K. Jain, 1989.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dctmtx.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dctmtx", *args, **kwargs)
