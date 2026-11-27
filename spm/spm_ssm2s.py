from spm._runtime import Runtime


def spm_ssm2s(*args, **kwargs):
    r"""
      Convert state-space (M) representation to eigenspectrum  
        FORMAT [s,u] = spm_ssm2s(P,M,TOL)  
         
        P    - model parameters  
        M    - model (with flow M.f and expansion point M.x and M.u)  
        TOL  - optional upper bound for  principality exponent  (default -4)  
         
        S    - (sorted) eigenspectrum or Lyapunov exponents  
        V    - associated eigenvectors  
         
        csd  - cross spectral density  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_ssm2s.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ssm2s", *args, **kwargs)
