from spm.__wrapper__ import Runtime


def spm_nlsi_Newton(*args, **kwargs):
    """
      Variational Lapalce for nonlinear models - Newton's method  
        FORMAT [Ep,Cp,F] = spm_nlsi_Newton(M,U,Y)  
         
        Eplicit log-likihood model  
       __________________________________________________________________________  
         
        M.L - log likelihood function @(P,M,U,Y)  
              P  - free parameters  
              M  - model  
         
        M.P  - starting estimates for model parameters [optional]  
        M.pE - prior expectation      - E{P}   of model parameters  
        M.pC - prior covariance       - Cov{P} of model parameters  
         
        U  - inputs or causes  
        Y  - output or response  
         
        Parameter estimates  
       --------------------------------------------------------------------------  
        Ep  - (p x 1)         conditional expectation    E{P|y}  
        Cp  - (p x p)         conditional covariance     Cov{P|y}  
         
        log evidence  
       --------------------------------------------------------------------------  
        F   - [-ve] free energy F = log evidence = p(Y|pE,pC) = p(y|m)  
         
       __________________________________________________________________________  
        Returns the moments of the posterior p.d.f. of the parameters of a  
        nonlinear model with a log likelihood function L(P,M,U,Y).  
         
        Priors on the free parameters P are specified in terms of expectation pE  
        and covariance pC. This Variational Laplace scheme uses an explicit  
        (numerical) curvature to implement a gradient ascent on variational free  
        energy using Newton's method. An example of its application is provided at  
        the end of this routine using a simple general linear model. This example  
        eschews the mean field approximation associated with standard  
        inversions.  
         
        For generic aspects of the scheme see:  
         
        Friston K, Mattout J, Trujillo-Barreto N, Ashburner J, Penny W.  
        Variational free energy and the Laplace approximation.  
        NeuroImage. 2007 Jan 1;34(1):220-34.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_nlsi_Newton.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_nlsi_Newton", *args, **kwargs)
