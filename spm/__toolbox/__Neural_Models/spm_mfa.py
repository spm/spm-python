from spm.__wrapper__ import Runtime


def spm_mfa(*args, **kwargs):
    """
      Jacobian for mean field approximations  
        FORMAT [M0,M1,L,X,q0] = spm_mfa(M,x,u)  
       --------------------------------------------------------------------------  
        M   - model specification structure  
        Required fields:  
           M.f   - dx/dt    = f(x,u,P)                     {function string or m-file}  
           M.g   - y(t)     = g(x,u,P)                     {function string or m-file}  
           M.m   - m inputs  
           M.n   - n states  
           M.l   - l ouputs  
           M.x   - (n x 1) = x(0) = expansion point  
           M.W   - (n x n) - covariance matrix of deterministic noise  
        x    - cell array of vectors specifying evaluation grid  
        u    - expansion point for inputs (c.f. background activity);  
         
        M0   - 1st order Bilinear matrix dq/dt = M0*q + u*M1*q,  q = p(X);  
        M1   - 2nd order Bilinear matrix  
        L    - output matrix                 <y> = L*q;  
        X    - evaluation points of state space  
        q0   - stable mode M0*q0 = 0  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_mfa.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mfa", *args, **kwargs)
