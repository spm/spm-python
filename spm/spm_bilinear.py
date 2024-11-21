from spm.__wrapper__ import Runtime


def spm_bilinear(*args, **kwargs):
    """
      Return global Volterra kernels for a MIMO Bilinear system  
        FORMAT [H0,H1,H2] = spm_bilinear(A,B,C,D,x0,N,dt)  
        A     - (n x n)     df(x(0),0)/dx                    - n states  
        B     - (n x n x m) d2f(x(0),0)/dxdu                 - m inputs  
        C     - (n x m)     df(x(0),0)/du - d2f(x(0),0)/dxdu*x(0)  
        D     - (n x 1)     f(x(0).0) - df(x(0),0)/dx*x(0)  
        x0    - (n x 1)     x(0)  
        N     - kernel depth       {intervals}  
        dt    - interval           {seconds}  
         
        Volterra kernels:  
         
        H0    - (n)                 = h0(t)         = y(t)  
        H1    - (N x n x m)         = h1i(t,s1)     = dy(t)/dui(t - s1)  
        H2    - (N x N x n x m x m) = h2ij(t,s1,s2) = d2y(t)/dui(t - s1)duj(t - s2)  
         
        where n = p if modes are specified  
         
       --------------------------------------------------------------------------  
        Returns Volterra kernels for bilinear systems of the form  
         
        dx/dt = f(x,u) = A*x + B1*x*u1 + ... Bm*x*um + C1u1 + ... Cmum + D  
         y(t) = x(t)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_bilinear.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_bilinear", *args, **kwargs)
