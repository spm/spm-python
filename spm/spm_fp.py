from spm.__wrapper__ import Runtime


def spm_fp(*args, **kwargs):
    """
      Fokker-Planck operators and equilibrium density for dynamic systems  
        FORMAT [M0,q0,X,x,f,M1,L] = spm_fp(M,x,u)  
       --------------------------------------------------------------------------  
        M   - model specification structure  
        Required fields:  
           M.f   - dx/dt    = f(x,u,P) or f(x,u,a,P)  {function string or m-file}  
           M.g   - y(t)     = g(x,u,P)                {function string or m-file}  
           M.m   - m inputs  
           M.n   - n states  
           M.l   - l outputs  
           M.x   - (n x 1) = x(0) = expansion point  
           M.W   - (n x n) - precision matrix of state noise  
        x    - cell array of vectors specifying evaluation grid  
        u    - expansion point for inputs or causes;  
         
        M0   - 1st order FP operator dq/dt = M0*q + u*M1*q,  q = p(X);  
        q0   - stable or equilibrium mode: M0*q0 = 0  
        X    - evaluation points of state space  
        x    - cell array of vectors specifying evaluation grid  
        f    - flow  
        M1   - 2nd order FP operator  
        L    - output matrix                 <y> = L*q;  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_fp.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fp", *args, **kwargs)
