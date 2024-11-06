from spm.__wrapper__ import Runtime


def spm_nlsi_LS(*args, **kwargs):
    """
      Bayesian inversion of a nonlinear model using (Laplacian) sampling  
        FORMAT [Ep,Cp,Eh,F] = spm_nlsi_LS(M,U,Y)  
         
        Dynamical MIMO models  
       __________________________________________________________________________  
         
        M.IS - function name f(P,M,U) - generative model  
               This function specifies the nonlinear model:  
               y = Y.y = IS(P,M,U) + X0*P0 + e  
               were e ~ N(0,C).  For dynamic systems this would be an integration  
               scheme (e.g. spm_int). spm_int expects the following:  
         
            M.f  - f(x,u,P,M)  
            M.g  - g(x,u,P,M)  
              x  - state variables  
              u  - inputs or causes  
              P  - free parameters  
              M  - fixed functional forms and parameters in M  
         
        M.FS - function name f(y,M)   - feature selection  
               This [optional] function performs feature selection assuming the  
               generalized model y = FS(y,M) = FS(IS(P,M,U),M) + X0*P0 + e  
         
        M.P  - starting estimates for model parameters [optional]  
         
        M.pE - prior expectation  - E{P}   of model parameters  
        M.pC - prior covariance   - Cov{P} of model parameters  
         
        M.hE - prior expectation  - E{h}   of log-precision parameters  
        M.hC - prior covariance   - Cov{h} of log-precision parameters  
         
        U.u  - inputs  
        U.dt - sampling interval  
         
        Y.y  - outputs  
        Y.dt - sampling interval for outputs  
        Y.X0 - Confounds or null space      (over size(y,1) bins or all vec(y))  
        Y.Q  - q error precision components (over size(y,1) bins or all vec(y))  
         
         
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
        and covariance pC.  
         
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_nlsi_LS.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_nlsi_LS", *args, **kwargs)
