from spm.__wrapper__ import Runtime


def spm_dcm_delay(*args, **kwargs):
    """
      Delay operator for flow and Jacobians of dynamical systems  
        FORMAT [Q,J] = spm_dcm_delay(P,M,J,N)  
        P   - model parameters  
        M   - model specification structure  
        J   - optional: system Jacobian  
        N   - optional: auto Taylor expansion [default: 2^8]  
         
        Required fields:  
          M.f - dx/dt    = f(x,u,P,M)            {function string or m-file}  
          M.m - m inputs  
          M.n - n states  
          M.x - (n x 1) = x(0) = expansion point: defaults to x = 0;  
          M.u - (m x 1) = u    = expansion point: defaults to u = 0;  
         
         
        Returns the delay operator for Jacobians of dynamical systems where the  
        states are  
         
        f     - dx(t)/dt  = f(x(t))  
        Q     - delay operator dx(t)/dt = f(x(t - d))  
                                        = Q(d)*f(x(t))  
        J     - Jacobian  = df/dt = (where delayed Jacobian = Q*J)  
         
        If the delay matrix is not specified it is computed from its parameters in  
        P.D (and M.pF.D if specified).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_delay.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_delay", *args, **kwargs)
