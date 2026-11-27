from spm._runtime import Runtime


def spm_ness_hd(*args, **kwargs):
    r"""
      Nonequilibrium steady-state under a Helmholtz decomposition  
        FORMAT NESS = spm_ness_hd(M,x)  
       --------------------------------------------------------------------------  
        M   - model specification structure  
        Required fields:  
           M.f   - dx/dt   = f(x,u,P)  {function string or m-file}  
           M.pE  - P       = parameters of equation of motion  
           M.x   - (n x 1) = x(0) = expansion point  
           M.W   - (n x n) - precision matrix of random fluctuations  
        x    - cell array of vectors specifying evaluation grid  
         
        NESS.Ep - parameters of log NESS  
        NESS.p0 - nonequilibrium steady-state  
        NESS.X  - evaluation points of state space  
        NESS.F  - expected flow  
        NESS.f  - original flow  
         
        NESS.H  - expected Hessian  
        NESS.J  - expected Jacobian  
        NESS.E  - Lyapunov exponents  
        NESS.H2 - expected Euclidean norm of Hessian  
        NESS.J2 - expected Euclidean norm of Jacobian  
        NESS.D2 - correlation dimension  
        NESS.o  - parameter orders  
         
        This routine returns the polynomial coefficients of a Laplace  
        approximation to nonequilibrium steady-state dynamics given some  
        equations of motion, which themselves could be based upon a Helmholtz  
        decomposition with a different polynomial expansion. In other words, it  
        converts a more or less expressive parameterisation of density dynamics  
        into a second order Laplace approximation that is suitable for solving  
        density dynamics.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_ness_hd.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ness_hd", *args, **kwargs)
