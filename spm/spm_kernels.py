from spm.__wrapper__ import Runtime


def spm_kernels(*args, **kwargs):
    """
      Return global Volterra kernels for a MIMO Bilinear system  
        FORMAT [K0,K1,K2] = spm_kernels(M,P,N,dt)            - output kernels  
        FORMAT [K0,K1,K2] = spm_kernels(M0,M1,N,dt)          - state  kernels  
        FORMAT [K0,K1,K2] = spm_kernels(M0,M1,L1,N,dt)       - output kernels (1st)  
        FORMAT [K0,K1,K2] = spm_kernels(M0,M1,L1,L2,N,dt)    - output kernels (2nd)  
         
        M,P   - model structure and parameters;   
                or its bilinear reduction:  
         
        M0    - (n x n)     df(q(0),0)/dq                    - n states  
        M1    - {m}(n x n)  d2f(q(0),0)/dqdu                 - m inputs  
        L1    - (l x n)     dldq                             - l outputs  
        L2    - {m}(n x n)  dl2dqq  
         
        N     - kernel depth       {intervals}  
        dt    - interval           {seconds}  
         
        Volterra kernels:  
       --------------------------------------------------------------------------  
        K0    - (1 x l)             = K0(t)         = y(t)  
        K1    - (N x l x m)         = K1i(t,s1)     = dy(t)/dui(t - s1)  
        K2    - (N x N x l x m x m) = K2ij(t,s1,s2) = d2y(t)/dui(t - s1)duj(t - s2)  
         
       __________________________________________________________________________  
         
        Returns Volterra kernels for bilinear systems of the form  
         
                dq/dt   = f(q,u) = M0*q + M1{1}*q*u1 + ... M1{m}*q*um  
                   y(i) = L1(i,:)*q + q'*L2{i}*q  
         
        where q = [1 x(t)] are the states augmented with a constant term  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_kernels.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_kernels", *args, **kwargs)
