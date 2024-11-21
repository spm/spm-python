from spm.__wrapper__ import Runtime


def spm_dx(*args, **kwargs):
    """
      Returns dx(t) = (expm(dfdx*t) - I)*inv(dfdx)*f  
        FORMAT [dx] = spm_dx(dfdx,f,[t])  
        dfdx   = df/dx  
        f      = dx/dt  
        t      = integration time: (default t = Inf);  
                 if t is a cell (i.e., {t}) then t is set to:  
                 exp(t - log(diag(-dfdx))  
         
        dx     = x(t) - x(0)  
       --------------------------------------------------------------------------  
        Integration of a dynamic system using local linearisation.  This scheme  
        accommodates nonlinearities in the state equation by using a functional  
        of f(x) = dx/dt.  This uses the equality  
         
                    expm([0   0     ]) = (expm(t*dfdx) - I)*inv(dfdx)*f  
                         [t*f t*dfdx]  
         
        When t -> Inf this reduces to  
         
                     dx(t) = -inv(dfdx)*f  
         
        These are the solutions to the gradient ascent ODE  
         
                   dx/dt   = k*f = k*dfdx*x =>  
         
                   dx(t)   = expm(t*k*dfdx)*x(0)  
                           = expm(t*k*dfdx)*inv(dfdx)*f(0) -  
                             expm(0*k*dfdx)*inv(dfdx)*f(0)  
         
        When f = dF/dx (and dfdx = dF/dxdx), dx represents the update from a  
        Gauss-Newton ascent on F.  This can be regularised by specifying {t}. A  
        heavy regularization corresponds to t = -4 and a light regularization  
        would be t = 4. This version of spm_dx uses an augmented system and the  
        Pade approximation to compute requisite matrix exponentials.  
         
        References:  
         
        Friston K, Mattout J, Trujillo-Barreto N, Ashburner J, Penny W. (2007).  
        Variational free energy and the Laplace approximation. NeuroImage.  
        34(1):220-34  
         
        Ozaki T (1992) A bridge between nonlinear time-series models and  
        nonlinear stochastic dynamical systems: A local linearization approach.  
        Statistica Sin. 2:113-135.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dx.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dx", *args, **kwargs)
