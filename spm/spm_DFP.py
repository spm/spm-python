from spm.__wrapper__ import Runtime


def spm_DFP(*args, **kwargs):
    """
      Dynamic free-energy Fokker-Planck free-form scheme  
        FORMAT [DEM] = spm_DFP(DEM)  
         
        DEM.M  - hierarchical model  
        DEM.Y  - output or data  
        DEM.U  - inputs or prior expectation of causes  
        DEM.X  - confounds  
       __________________________________________________________________________  
         
        generative model  
       --------------------------------------------------------------------------  
          M(i).g  = y(t)  = g(x,v,P)    {inline function, string or m-file}  
          M(i).f  = dx/dt = f(x,v,P)    {inline function, string or m-file}  
         
          M(i).pE = prior expectation of p model-parameters  
          M(i).pC = prior covariances of p model-parameters  
          M(i).hE = prior expectation of h hyper-parameters (input noise)  
          M(i).hC = prior covariances of h hyper-parameters (input noise)  
          M(i).gE = prior expectation of g hyper-parameters (state noise)  
          M(i).gC = prior covariances of g hyper-parameters (state noise)  
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
          qU.e    = Conditional residuals  
          qU.C    = Conditional covariance: cov(v)  
          qU.S    = Conditional covariance: cov(x)  
         
        conditional moments of model-parameters - q(p)  
       --------------------------------------------------------------------------  
          qP.P    = Conditional expectation  
          qP.Pi   = Conditional expectation for each level  
          qP.C    = Conditional covariance  
           
        conditional moments of hyper-parameters (log-transformed) - q(h)  
       --------------------------------------------------------------------------  
          qH.h    = Conditional expectation  
          qH.hi   = Conditional expectation for each level  
          qH.C    = Conditional covariance  
          qH.iC   = Component  precision: cov(vec(e[:})) = inv(kron(iC,iV))  
          qH.iV   = Sequential precision  
         
        F         = log evidence = marginal likelihood = negative free energy  
       __________________________________________________________________________  
         
        spm_DFP implements a variational Bayes (VB) scheme under the Laplace  
        approximation to the conditional densities of the model's, parameters (p)  
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
         
        The D-step is implemented with variational filtering, which does not  
        assume a fixed form for the conditional density; it uses the sample  
        density of an ensemble of particles that drift up free-energy gradients  
        and 'explore' the local curvature though (Wiener) perturbations.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_DFP.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_DFP", *args, **kwargs)
