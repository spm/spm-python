from spm._runtime import Runtime


def spm_NESS_gen_lap(*args, **kwargs):
    r"""
      Generate flow (F) at locations x  
        FORMAT [F,S,Q,L,H,D,E] = spm_NESS_gen_lap(P,M)  
        FORMAT [F,S,Q,L,H,D,E] = spm_NESS_gen_lap(P,M,x)  
        FORMAT [F,S,Q,L,H,D,E] = spm_NESS_gen_lap(P,M,U)  
       --------------------------------------------------------------------------  
        P.Qp    - polynomial coefficients for solenoidal operator  
        P.Sp    - polynomial coefficients for Kernel (suprisal)  
        P.Rp    - polynomial coefficients for mean   (suprisal)  
         
        F       - polynomial approximation to flow  
        S       - negative potential (log NESS density)  
        Q       - flow operator (R + G) with solenoidal and symmetric parts  
        L       - correction term for derivatives of solenoidal flow  
        H       - Hessian  
        D       - potential gradients  
        E       - expectation of NESS density  
         
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
        U.dLdp  - gradients of L  w.r.t. flow parameters  
         
        This routine returns the flow at a number of specified points in state  
        space under a polynomial approximation to any Helmholtz-Hodge  
        decomposition of nonequilibrium steady-state dynamics. This routine  
        shares many of the same constructs as spm_NESS_fx; with the exception  
        that the dissipative part of the flow (i.e., amplitude of random  
        fluctuations G) is specified as the precision of a state-space model:  
        M.W.  
         
        In brief, spm_NESS_fx returns the flow for a particular point in state  
        space, whereas this routine returns the flow for an arbitrary number of  
        points at the same time. These flows can then be used as a generative  
        model for the flow sampled over grid points in state space—or during the  
        evolution of some path through state space.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_NESS_gen_lap.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_NESS_gen_lap", *args, **kwargs)
