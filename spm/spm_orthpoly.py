from spm.__wrapper__ import Runtime


def spm_orthpoly(*args, **kwargs):
    """
      Create orthonormal polynomial basis functions  
        FORMAT C = spm_orthpoly(N,[K])  
        N - dimension  
        K - order  
       __________________________________________________________________________  
         
        spm_orthpoly creates a matrix for the first few basis functions of an  
        orthogonal polynomial expansion.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_orthpoly.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_orthpoly", *args, **kwargs)
