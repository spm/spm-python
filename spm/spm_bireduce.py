from spm.__wrapper__ import Runtime


def spm_bireduce(*args, **kwargs):
    """
      Reduction of a fully nonlinear MIMO system to Bilinear form  
        FORMAT [M0,M1,L1,L2] = spm_bireduce(M,P)  
         
        M   - model specification structure  
        Required fields:  
          M.f   - dx/dt    = f(x,u,P,M)                 {function string or m-file}  
          M.g   - y(t)     = g(x,u,P,M)                 {function string or m-file}  
          M.bi  - bilinear form [M0,M1,L1,L2] = bi(M,P) {function string or m-file}  
          M.m   - m inputs  
          M.n   - n states  
          M.l   - l outputs  
          M.x   - (n x 1) = x(0) = expansion point: defaults to x = 0;  
          M.u   - (m x 1) = u    = expansion point: defaults to u = 0;  
         
          M.D   - delay operator df/dx -> D*df/dx [optional]  
         
        P   - model parameters  
         
        A Bilinear approximation is returned where the states are  
         
               q(t) = [1; x(t) - x(0)]  
         
       __________________________________________________________________________  
        Returns Matrix operators for the Bilinear approximation to the MIMO  
        system described by  
         
              dx/dt = f(x,u,P)  
               y(t) = g(x,u,P)  
         
        evaluated at x(0) = x and u = 0  
         
              dq/dt = M0*q + u(1)*M1{1}*q + u(2)*M1{2}*q + ....  
               y(i) = L1(i,:)*q + q'*L2{i}*q/2;  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_bireduce.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_bireduce", *args, **kwargs)
