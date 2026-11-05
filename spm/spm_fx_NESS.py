from spm._runtime import Runtime


def spm_fx_NESS(*args, **kwargs):
    r"""
      Generate flow (f) at locations x  
        FORMAT f = spm_fx_NESS(x,u,P,M)  
       --------------------------------------------------------------------------  
        x       - latent states  
        u       - exogenous input  
        P.Qp    - polynomial coefficients for solenoidal operator  
        P.Sp    - polynomial coefficients for kernel (suprisal)  
        P.Rp    - polynomial coefficients for mean   (suprisal)  
        P.W     - precision of random fluctuations  
         
        f       - polynomial approximation to flow  
        S       - surprisal or negative (log NESS density)  
        Q       - flow operator (R + G) with solenoidal and symmetric parts  
        L       - correction term for derivatives of solenoidal flow  
        H       - Hessian  
         
        U = spm_NESS_U(x)  
       --------------------------------------------------------------------------  
        U.b     - polynomial basis  
        U.D     - derivative operator  
        U.dbQdp - gradients of bQ w.r.t. flow parameters  
         
        flow  (Jacobian J = df/dx)  
       --------------------------------------------------------------------------  
          S     = -ln(p(x)) = x*H*x'/2;  
          dS/dx = H*x  
          f     = -(R + G)*dS/dx  = -Q*dS/dx = -Q*H*x  
          df/dx = -(R + G)*H      = -Q*H = J   
          H     = K'*K  
          G     = inv(W)/2;  
         
        This routine returns the flow or dynamics of a nonequilibrium  
        steady-state model, parameterised under the Helmholtz-Hodge decomposition  
        (up to 2nd order) in terms of flow operators Q and surprisal gradients.  
        The flow has solenoidal (R) and dissipative (G) parts, while the  
        surprisal S or self-information is parameterised to 2nd order, with the  
        proviso that the requisite Hessian (i.e., precision of the nonequilibrium  
        steady-state density) is itself state-dependent to 1st order (by  
        parameterising the Hessian in terms of the outer product of a surprisal  
        kernel with itself H = K’*K. The underlying surprisal or log Ness  
        density, the flow operators and the Hessian can also be returned by  
        increasing the number of output arguments.  
         
        NB: these output arguments are suppressed in the current code because the  
        accompanying inversion schemes expect the Jacobian to be returned as the  
        second argument. And the Jacobian is most simply evaluated numerically,  
        or with automatic differentiation.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_fx_NESS.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_fx_NESS", *args, **kwargs)
