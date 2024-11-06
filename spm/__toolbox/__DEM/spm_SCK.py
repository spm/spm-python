from spm.__wrapper__ import Runtime


def spm_SCK(*args, **kwargs):
    """
      FORMAT SCKS = spm_SCK(SCKS)  
       __________________________________________________________________________  
        Square-root Cubature Kalman Filters [2] & Square-root Rauch-Tang-Striebel  
        Smoother (SCKF-SCKS [1]).  
       ==========================================================================  
        This function performs joint estimation of the states, input and parameters  
        of a model that is described as a stochastic continuous-discrete   
        state-space in terms of nonlinear blind deconvolution. The state equations  
        must have the form of ordinary differential equations, where the   
        discretization is performed through local-linearization scheme [3].   
        Additionally, the parameter noise covariance is estimated online via   
        stochastic Robbins-Monro approximation method [4], and the measurement noise   
        covariance is estimated using a combined variational Bayesian (VB)   
        approach with a nonlinear filter/smoother [5].  
       __________________________________________________________________________  
         
        SCKS.M  - model structure (based on DEM [6] in SPM8 toolbox)  
        SCKS.Y  - response variable, output or data  
       __________________________________________________________________________  
         
        generative model:  
       --------------------------------------------------------------------------  
          M(1).f  = dx/dt = f(x,v,P)    {inline function, string or m-file}  
          M(1).g  = y(t)  = g(x,v,P)    {inline function, string or m-file}  
            
          M(1).xP = state error covariance matrix  
          M(1).uP = input error variance  
          M(1).wP = parameter error covariance matrix  
         
          M(1).pE = prior expectation of p model-parameters  
          M(1).pC = prior covariances of p model-parameters  
          M(1).ip = parameter indices  
          M(1).cb = constrain on parameters [lower, upper];  
         
          M(1).Q  = precision components on observation noise  
          M(1).V  = fixed precision (input noise)  
          M(1).W  = precision on state noise (approximated by annealing)  
         
          M(i).m  = number of inputs v(i + 1);  
          M(1).n  = number of states x(i);  
          M(1).l  = number of output v(i);  
         
          M(1).Qf      = form of measurement noise cov estimate:  
                         'auto'[default],'min','mean'  
          M(1).E.nN    = number of SCKF-SCKS algorithm iterations  
          M(1).E.Itol  = tolerance value for SCKF-SCKS convergence   
          M(1).E.nD    = number of integration step between observations  
          M(1).VB.N    = number of VB algorithm iterations  
          M(1).VB.Itol = tolerance value for VB convergence   
          M(1).VB.l    = VB scaling factor;  
         
          conditional moments of model-states - q(u)  
       --------------------------------------------------------------------------  
          qU.x  = Conditional expectation of hidden states (backward estimate)  
          qU.v  = Conditional expectation of input (backward estimate)  
          qU.z  = Conditional prediction error   
          qU.S  = Conditional covariance: cov(x) (states - backward estimate)  
          qU.C  = Conditional covariance: cov(u) (input - backward estimate)  
         
        conditional moments of model-parameters - q(p)  
       --------------------------------------------------------------------------  
          qP.P    = Conditional expectation  
          qP.C    = Conditional covariance  
         
             F    = negative log-likelihood  
       __________________________________________________________________________  
        Copyright (c) Brno University of Technology (2010)...  
        Martin Havlicek 05-12-2010  
          
        References:  
        [1] Havlicek M et al (2011)  
        [2] Arasaratnam, I., Haykin, S. (2009) Cubature Kalman Filters. IEEE  
            Transactions on Automatic Control 54, 1254-1269.  
        [3] Jimenez, J.C. (2002) A simple algebraic expression to evaluate the  
            local linearization schemes for stochastic differential equations*   
            1. Applied Mathematics Letters 15, 775-780.  
        [4] Van der Merwe, R., 2004. Sigma-point Kalman filters for probabilistic  
            inference in dynamic state-space models. Ph.D.thesis, Oregon Graduate   
            Institute of Science and Technology.  
        [5] Sarkka, S., Hartikainen, J. (2011?) Extension of VB-AKF to Estimation  
            of Full Covariance and Non-Linear Systems. In Press.  
        [6] Friston, K.J., et al. (2008) DEM: a variational treatment of dynamic  
            systems. Neuroimage 41, 849-885.  
       __________________________________________________________________________  
        Copyright (C) - Martin Havlicek  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_SCK.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_SCK", *args, **kwargs)
