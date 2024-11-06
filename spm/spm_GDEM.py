from spm.__wrapper__ import Runtime


def spm_GDEM(*args, **kwargs):
    """
      Dynamic expectation maximisation:  Generation and inversion  
        FORMAT DEM = spm_GDEM(DEM)  
         
        DEM.G  - generation model  
        DEM.M  - inversion model  
        DEM.C  - causes  
        DEM.U  - prior expectation of causes  
       __________________________________________________________________________  
         
        This implementation of DEM is the same as spm_DEM but integrates both the  
        generative and inversion models in parallel. Its functionality is exactly  
        the same apart from the fact that confounds are not accommodated  
        explicitly.  The generative model is specified by DEM.G and the veridical  
        causes by DEM.C; these may or may not be used as priors on the causes for  
        the inversion model DEM.M (i..e, DEM.U = DEM.C).  Clearly, DEM.G does not  
        requires any priors or precision components; it will use the values of the  
        parameters specified in the prior expectation fields.  
         
        This routine is not used for model inversion per se but the simulate the  
        dynamical inversion of models (as a preclude to coupling the model back to  
        the generative process (see spm_ADEM)  
         
        hierarchical models G(i) and M(i)  
       --------------------------------------------------------------------------  
          M(i).g  = y(t)  = g(x,v,P)    {inline function, string or m-file}  
          M(i).f  = dx/dt = f(x,v,P)    {inline function, string or m-file}  
         
          M(i).pE = prior expectation of p model-parameters  
          M(i).pC = prior covariances of p model-parameters  
          M(i).hE = prior expectation of h hyper-parameters (cause noise)  
          M(i).hC = prior covariances of h hyper-parameters (cause noise)  
          M(i).gE = prior expectation of g hyper-parameters (state noise)  
          M(i).gC = prior covariances of g hyper-parameters (state noise)  
          M(i).Q  = precision components (input noise)  
          M(i).R  = precision components (state noise)  
          M(i).V  = fixed precision (input noise)  
          M(i).W  = fixed precision (state noise)  
         
          M(i).m  = number of inputs v(i + 1);  
          M(i).n  = number of states x(i);  
          M(i).l  = number of output v(i);  
         
        Returns the following fields of DEM  
       --------------------------------------------------------------------------  
         
        true model-states - u  
       --------------------------------------------------------------------------  
          pU.x    = hidden states  
          pU.v    = causal states v{1} = response (Y)  
         
        model-parameters - p  
       --------------------------------------------------------------------------  
          pP.P    = parameters for each level  
         
        hyper-parameters (log-transformed) - h ,g  
       --------------------------------------------------------------------------  
          pH.h    = cause noise  
          pH.g    = state noise  
         
        conditional moments of model-states - q(u)  
       --------------------------------------------------------------------------  
          qU.x    = Conditional expectation of hidden states  
          qU.v    = Conditional expectation of causal states  
          qU.z    = Conditional prediction errors (v)  
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
        in generalised coordinates.  This means DEM can deconvolve online and can  
        represents an alternative to Kalman filtering or alternative Bayesian  
        update procedures.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_GDEM.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_GDEM", *args, **kwargs)
