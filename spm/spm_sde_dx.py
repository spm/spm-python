from spm.__wrapper__ import Runtime


def spm_sde_dx(*args, **kwargs):
    """
      Return dx(t) = (expm(dfdx*t) - I)*inv(dfdx)*f + w for SDEs  
        FORMAT [dx] = spm_sde_dx(dfdx,dfdw,f,t)  
        dfdx   = df/dx - x: states  
        dfdw   = df/dw - w: i.i.d. Weiner process   
        f      = dx/dt  
        t      = integration time: (default t = 1);  
         
        dx     = x(t) - x(0)  
       --------------------------------------------------------------------------  
        Integration of stochastic differential equations using local linearization.   
        This scheme accommodates nonlinearities in the state equation by using a   
        functional of f(x) = dx/dt.  This uses the equality  
         
                    expm([0    0]*t) = expm(dfdx*t) - I)*inv(dfdx)*f  
                         [f dfdx]  
         
        When t -> Inf this reduces to  
         
                     dx(t) = -inv(dfdx)*f  
         
        for the SDE:  dx = dfdx*x*dt + sqrt(2)*dfdw*dw  
         
        where w is a standard Wiener process. Unstable modes are removed using  
        the systems eigenmodes.  
         
        see also spm_dx  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_sde_dx.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_sde_dx", *args, **kwargs)
