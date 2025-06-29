from spm._runtime import Runtime


def spm_nlsi_GN(*args, **kwargs):
    """
      Bayesian inversion of nonlinear models - Gauss-Newton/Variational Laplace  
        FORMAT [Ep,Cp,Eh,F,L,dFdp,dFdpp] = spm_nlsi_GN(M,U,Y)  
         
        [Dynamic] MIMO models  
       __________________________________________________________________________  
        M.G  - or  
        M.IS - function name f(P,M,U) - generative model  
               This function specifies the nonlinear model:  
                 y = Y.y = IS(P,M,U) + X0*P0 + e  
               where e ~ N(0,C). For dynamic systems this would be an integration  
               scheme (e.g. spm_int). spm_int expects the following:  
         
            M.f  - f(x,u,P,M)  
            M.g  - g(x,u,P,M)  
            M.h  - h(x,u,P,M)  
              x  - state variables  
              u  - inputs or causes  
              P  - free parameters  
              M  - fixed functional forms and parameters in M  
         
        M.FS - function name f(y,M)   - feature selection  
               This [optional] function performs feature selection assuming the  
               generalized model y = FS(y,M) = FS(IS(P,M,U),M) + X0*P0 + e  
         
        M.P  - starting estimates for model parameters [optional]  
         
        M.pE - prior expectation      - E{P}   of model parameters  
        M.pC - prior covariance       - Cov{P} of model parameters  
         
        M.hE - prior expectation      - E{h}   of log-precision parameters  
        M.hC - prior covariance       - Cov{h} of log-precision parameters  
         
        U.u  - inputs (or just U)  
        U.dt - sampling interval  
         
        Y.y  - outputs (samples (time) x observations (first sort) x ...)  
        Y.dt - sampling interval for outputs  
        Y.X0 - confounds or null space      (over size(y,1) samples or all vec(y))  
        Y.Q  - q error precision components (over size(y,1) samples or all vec(y))  
         
         
        Parameter estimates  
       --------------------------------------------------------------------------  
        Ep  - (p x 1)         conditional expectation    E{P|y}  
        Cp  - (p x p)         conditional covariance     Cov{P|y}  
        Eh  - (q x 1)         conditional log-precisions E{h|y}  
         
        log evidence  
       --------------------------------------------------------------------------  
        F   - [-ve] free energy F = log evidence = p(y|f,g,pE,pC) = p(y|m)  
         
       __________________________________________________________________________  
        Returns the moments of the posterior p.d.f. of the parameters of a  
        nonlinear model specified by IS(P,M,U) under Gaussian assumptions.  
        Usually, IS is an integrator of a dynamic MIMO input-state-output model  
         
                     dx/dt = f(x,u,P)  
                     y     = g(x,u,P)  + X0*P0 + e  
         
        A static nonlinear observation model with fixed input or causes u  
        obtains when x = []. i.e.  
         
                     y     = g([],u,P) + X0*P0e + e  
         
        but static nonlinear models are specified more simply using  
         
                     y     = IS(P,M,U) + X0*P0 + e  
         
        Priors on the free parameters P are specified in terms of expectation pE  
        and covariance pC. The E-Step uses a Fisher-Scoring scheme and a Laplace  
        approximation to estimate the conditional expectation and covariance of P  
        If the free-energy starts to increase,  an abbreviated descent is  
        invoked.  The M-Step estimates the precision components of e, in terms  
        of log-precisions.  Although these two steps can be thought of in  
        terms of E and M steps they are in fact variational steps of a full  
        variational Laplace scheme that accommodates conditional uncertainty  
        over both parameters and log precisions (c.f. hyperparameters with hyper  
        priors).  
         
        An optional feature selection can be specified with parameters M.FS.  
         
        For generic aspects of the scheme see:  
         
        Friston K, Mattout J, Trujillo-Barreto N, Ashburner J, Penny W.  
        Variational free energy and the Laplace approximation.  
        NeuroImage. 2007 Jan 1;34(1):220-34.  
         
        This scheme handles complex data along the lines originally described in:  
         
        Sehpard RJ, Lordan BP, and Grant EH.  
        Least squares analysis of complex data with applications to permittivity  
        measurements.  
        J. Phys. D. Appl. Phys 1970 3:1759-1764.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_nlsi_GN.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_nlsi_GN", *args, **kwargs)
