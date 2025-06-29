from spm._runtime import Runtime


def spm_NESS_F(*args, **kwargs):
    """
      Generate flow (f) at locations (U.X)  
        FORMAT [F,S,Q,L,H,D] = spm_NESS_gen(P,M)  
        FORMAT [F,S,Q,L,H,D] = spm_NESS_gen(P,M,U)  
        FORMAT [F,S,Q,L,H,D] = spm_NESS_gen(P,M,X)  
       --------------------------------------------------------------------------  
        P.Qp    - polynomial coefficients for solenoidal operator  
        P.Sp    - polynomial coefficients for potential  
         
        F       - polynomial approximation to flow  
        S       - negative potential (log NESS density)  
        Q       - flow operator (R + G) with solenoidal and symmetric parts  
        L       - correction term for derivatives of solenoidal flow  
        H       - Hessian  
        D       - potential gradients  
         
        U = spm_ness_U(M)  
       --------------------------------------------------------------------------  
        M   - model specification structure  
        Required fields:  
           M.X  - sample points  
           M.W  - (n x n) - precision matrix of random fluctuations  
           M.K  - order of polynomial expansion  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_NESS_F.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_NESS_F", *args, **kwargs)
