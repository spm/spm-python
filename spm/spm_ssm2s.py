from spm.__wrapper__ import Runtime


def spm_ssm2s(*args, **kwargs):
    """
      Convert state-space (M) representation to eigenspectrum  
        FORMAT [s,u] = spm_ssm2s(P,M,TOL)  
         
        P    - model parameters  
        M    - model (with flow M.f and expansion point M.x and M.u)  
        TOL  - optional upper bound for  principality exponent  (default -4)  
         
        S    - (sorted) eigenspectrum or Lyapunov exponents  
        V    - associated eigenvectors  
         
        csd  - cross spectral density  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_ssm2s.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ssm2s", *args, **kwargs)
