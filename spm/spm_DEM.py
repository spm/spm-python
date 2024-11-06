from spm.__wrapper__ import Runtime


def spm_DEM(*args, **kwargs):
    """
      Dynamic expectation maximisation (Variational Laplacian filtering)  
        FORMAT DEM   = spm_DEM(DEM)  
         
        DEM.M  - hierarchical model  
        DEM.Y  - response variable, output or data  
        DEM.U  - explanatory variables, inputs or prior expectation of causes  
        DEM.X  - confounds  
       __________________________________________________________________________  
         
        generative model  
       --------------------------------------------------------------------------  
          M(i).g  = y(t)  = g(x,v,P)    {inline function, string or m-file}  
          M(i).f  = dx/dt = f(x,v,P)    {inline function, string or m-file}  
         
          M(i).pE = prior expectation of p model-parameters  
          M(i).pC = prior covariances of p model-parameters  
          M(i).hE = prior expectation of h log-precision (cause noise)  
          M(i).hC = prior covariances of h log-precision (cause noise)  
          M(i).gE = prior expectation of g log-precision (state noise)  
          M(i).gC = prior covariances of g log-precision (state noise)  
          M(i).Q  = precision components (input noise)  
          M(i).R  = precision components (state noise)  
          M(i).V  = fixed precision (input noise)  
          M(i).W  = fixed precision (state noise)  
          M(i).xP = precision (states)  
         
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
         
        F         = log evidence = log marginal likelihood = negative free energy  
       __________________________________________________________________________  
         
        spm_DEM implements a variational Bayes (VB) scheme under the Laplace  
        approximation to the conditional densities of states (u), parameters (p)  
        and hyperparameters (h) of any analytic nonlinear hierarchical dynamic  
        model, with additive Gaussian innovations.  It comprises three  
        variational steps (D,E and M) that update the conditional moments of u, p  
        and h respectively  
         
                       D: qu.u = max <L>q(p,h)  
                       E: qp.p = max <L>q(u,h)  
                       M: qh.h = max <L>q(u,p)  
         
        where qu.u corresponds to the conditional expectation of hidden states x  
        and causal states v and so on.  L is the ln p(y,u,p,h|M) under the model  
        M. The conditional covariances obtain analytically from the curvature of  
        L with respect to u, p and h.  
         
        The D-step is embedded in the E-step because q(u) changes with each  
        sequential observation.  The dynamical model is transformed into a static  
        model using temporal derivatives at each time point.  Continuity of the  
        conditional trajectories q(u,t) is assured by a continuous ascent of F(t)  
        in generalised coordinates.  This means DEM can deconvolve online and  
        can represents an alternative to Kalman filtering or alternative Bayesian  
        update procedures.  
         
         
        To accelerate computations one can specify the nature of the model using  
        the field:  
         
        M(1).E.linear = 0: full        - evaluates 1st and 2nd derivatives  
        M(1).E.linear = 1: linear      - equations are linear in x and v  
        M(1).E.linear = 2: bilinear    - equations are linear in x, v and x.v  
        M(1).E.linear = 3: nonlinear   - equations are linear in x, v, x.v, and x.x  
        M(1).E.linear = 4: full linear - evaluates 1st derivatives (for generalised   
                                         filtering, where parameters change)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_DEM.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_DEM", *args, **kwargs)
