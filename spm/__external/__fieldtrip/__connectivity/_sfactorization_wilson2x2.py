from spm.__wrapper__ import Runtime


def _sfactorization_wilson2x2(*args, **kwargs):
    """
      SFACTORIZATION_WILSON2X2 performs pairwise non-parametric spectral factorization on  
        cross-spectra, based on Wilson's algorithm.  
         
        Usage  : [H, Z, psi] = sfactorization_wilson(S,freq);  
         
        Inputs : S (1-sided, 3D-spectral matrix in the form of Channel x Channel x frequency)   
               : freq (a vector of frequencies) at which S is given.   
         
        Outputs: H (transfer function)  
               : Z (noise covariance)  
               : S (cross-spectral density 1-sided)  
               : psi (left spectral factor)  
         
        This function is an implemention of Wilson's algorithm (Eq. 3.1)  
        for spectral matrix factorization.  
         
        Ref: G.T. Wilson,"The Factorization of Matricial Spectral Densities,"  
        SIAM J. Appl. Math.23,420-426(1972).  
        Written by M. Dhamala & G. Rangarajan, UF, Aug 3-4, 2006.  
        Email addresses: mdhamala@bme.ufl.edu, rangaraj@math.iisc.ernet.in  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/private/sfactorization_wilson2x2.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("sfactorization_wilson2x2", *args, **kwargs)
