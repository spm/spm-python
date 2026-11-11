from spm._runtime import Runtime


def spm_ness_U(*args, **kwargs):
    r"""
      basis functions for NESS under a Helmholtz decomposition  
        FORMAT U = spm_ness_U(M,x)  
       --------------------------------------------------------------------------  
        M   - model specification structure  
        Required fields:  
          [M.f   - dx/dt   = f(x,u,P)  {function string or m-file}]  
          [M.pE  - P       = parameters of equation of motion]  
           M.x   - (n x 1) = x(0) = expansion point  
           M.W   - (n x n) - precision matrix of random fluctuations  
           M.X   - sample points  
           M.K   - order of polynomial expansion (suprisal)  
           M.L   - order of polynomial expansion (solenoidal)  
         
        x       - sample points  
         
        U.x     - domain  
        U.X     - sample points  
        [U.f    - expected flow at sample points]  
        [U.J    - Jacobian at sample points]  
        U.b     - polynomial basis  
        U.D     - derivative operator  
        U.G     - amplitude of random fluctuations  
        U.H     - Hessian operator  
        U.dQdp  - gradients of flow operator Q  w.r.t. flow parameters  
        U.dbQdp - gradients of bQ w.r.t. flow parameters  
        U.dLdp  - gradients of L w.r.t. flow parameters  
        U.nx    - dimensions  
        U.o     - orders  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_ness_U.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ness_U", *args, **kwargs)
