from spm.__wrapper__ import Runtime


def spm_LAPS(*args, **kwargs):
    """
      Laplacian model inversion (with smoothness hyperparameter optimisation)  
        FORMAT DEM = spm_LAPS(DEM)  
         
        DEM.M  - hierarchical model  
        DEM.Y  - response variable, output or data  
        DEM.U  - explanatory variables, inputs or prior expectation of causes  
       __________________________________________________________________________  
         
        generative model  
       --------------------------------------------------------------------------  
          M(i).g  = v     =  g(x,v,P)   {inline function, string or m-file}  
          M(i).f  = dx/dt =  f(x,v,P)   {inline function, string or m-file}  
         
          M(i).ph = pi(v) = ph(x,v,h,M) {inline function, string or m-file}  
          M(i).pg = pi(x) = pg(x,v,g,M) {inline function, string or m-file}  
         
          M(i).pE = prior expectation of p model-parameters  
          M(i).pC = prior covariances of p model-parameters  
          M(i).hE = prior expectation of h log-precision (cause noise)  
          M(i).hC = prior covariances of h log-precision (cause noise)  
          M(i).gE = prior expectation of g log-precision (state noise)  
          M(i).gC = prior covariances of g log-precision (state noise)  
          M(i).xP = precision (states)  
          M(i).Q  = precision components (input noise)  
          M(i).R  = precision components (state noise)  
          M(i).V  = fixed precision (input noise)  
          M(i).W  = fixed precision (state noise)  
         
          M(i).m  = number of inputs v(i + 1);  
          M(i).n  = number of states x(i);  
          M(i).l  = number of output v(i);  
         
        conditional moments of model-states - q(u)  
       --------------------------------------------------------------------------  
          qU.x    = Conditional expectation of hidden states  
          qU.v    = Conditional expectation of causal states  
          qU.w    = Conditional prediction error (states)  
          qU.z    = Conditional prediction error (causes)  
          qU.C    = Conditional covariance: cov(v)  
          qU.S    = Conditional covariance: cov(x)  
         
        conditional moments of model-parameters - q(p)  
       --------------------------------------------------------------------------  
          qP.P    = Conditional expectation  
          qP.C    = Conditional covariance  
         
        conditional moments of hyper-parameters (log-transformed) - q(h)  
       --------------------------------------------------------------------------  
          qH.h    = Conditional expectation (cause noise)  
          qH.g    = Conditional expectation (state noise)  
          qH.C    = Conditional covariance  
         
        F         = log-evidence = log-marginal likelihood = negative free-energy  
       __________________________________________________________________________  
         
        spm_LAP implements a variational scheme under the Laplace  
        approximation to the conditional joint density q on states (u), parameters   
        (p) and hyperparameters (h,g) of any analytic nonlinear hierarchical dynamic  
        model, with additive Gaussian innovations.  
         
                   q(u,p,h,g) = max <L(t)>q  
         
        L is the ln p(y,u,p,h,g|M) under the model M. The conditional covariances  
        obtain analytically from the curvature of L with respect to the unknowns.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_LAPS.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_LAPS", *args, **kwargs)
