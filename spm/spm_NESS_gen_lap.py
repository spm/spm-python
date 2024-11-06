from spm.__wrapper__ import Runtime


def spm_NESS_gen_lap(*args, **kwargs):
    """
      Generate flow (f) at locations x  
        FORMAT [F,S,Q,L,H,D] = spm_NESS_gen_lap(P,M,x)  
        FORMAT [F,S,Q,L,H,D] = spm_NESS_gen_lap(P,M,U)  
       --------------------------------------------------------------------------  
        P.Qp    - polynomial coefficients for solenoidal operator  
        P.Sp    - polynomial coefficients for Kernel  
        P.Rp    - polynomial coefficients for mean  
         
        F       - polynomial approximation to flow  
        S       - negative potential (log NESS density)  
        Q       - flow operator (R + G) with solenoidal and symmetric parts  
        L       - correction term for derivatives of solenoidal flow  
        H       - Hessian  
        D       - potential gradients  
         
        U = spm_ness_U(M)  
       --------------------------------------------------------------------------  
        M   - model specification structure  
         
        U       - domain (of state space) structure  
        U.x     - domain  
        U.X     - sample points  
        U.f     - expected flow at sample points  
        U.J     - Jacobian at sample points  
        U.b     - polynomial basis  
        U.D     - derivative operator  
        U.G     - amplitude of random fluctuations  
        U.bG    - projection of flow operator (symmetric part: G)  
        U.dQdp  - gradients of flow operator Q  w.r.t. flow parameters  
        U.dbQdp - gradients of bQ w.r.t. flow parameters  
        U.dLdp  - gradients of L w.r.t. flow parameters  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_NESS_gen_lap.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_NESS_gen_lap", *args, **kwargs)
