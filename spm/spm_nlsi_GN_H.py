from spm.__wrapper__ import Runtime


def spm_nlsi_GN_H(*args, **kwargs):
    """
      Bayesian inversion of a nonlinear model with hierarchical optimisation  
        FORMAT [Ep,Cp,Eh,F] = spm_nlsi_GN_H(M,U,Y)  
         
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
         
        U.u  - inputs (or just U)  
        U.dt - sampling interval  
         
        Y.y  - outputs (samples x observations)  
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
        This is the same as spm_nlsi_GN but tries to model the free energy as a  
        function of conditional expectations using a sparse mixture of scaled  
        Gaussians. The objective is to account for local maxima when optimising  
        free energy by recasting the problem in terms of a parameterised mapping   
        from conditional expectations to free energy explicitly.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_nlsi_GN_H.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_nlsi_GN_H", *args, **kwargs)
