from spm._runtime import Runtime


def spm_orthpoly(*args, **kwargs):
    r"""
      Create orthonormal polynomial basis functions  
        FORMAT C = spm_orthpoly(N,[K])  
        N - dimension  
        K - order  
       __________________________________________________________________________  
         
        spm_orthpoly creates a matrix for the first few basis functions of an  
        orthogonal polynomial expansion.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_orthpoly.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_orthpoly", *args, **kwargs)
