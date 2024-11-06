from spm.__wrapper__ import Runtime


def spm_dcm_csd_priors(*args, **kwargs):
    """
      Optimisation of priors  
        FORMAT [pE] = spm_dcm_csd_priors(M,U,Y,k)  
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
         
        k    - indices of parameter vector to search over  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_csd_priors.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_csd_priors", *args, **kwargs)
