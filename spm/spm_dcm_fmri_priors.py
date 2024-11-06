from spm.__wrapper__ import Runtime


def spm_dcm_fmri_priors(*args, **kwargs):
    """
      Return the priors for a two-state DCM for fMRI  
        FORMAT [pE,pC,x,vC] = spm_dcm_fmri_priors(A,B,C,D,options)  
         
          options.two_state:  (0 or 1) one or two states per region  
          options.stochastic: (0 or 1) exogenous or endogenous fluctuations  
          options.precision:           log precision on connection rates  
         
        INPUT:  
           A,B,C,D - constraints on connections (1 - present, 0 - absent)  
         
        OUTPUT:  
           pE     - prior expectations (connections and hemodynamic)  
           pC     - prior covariances  (connections and hemodynamic)  
           x      - prior (initial) states  
           vC     - prior variances    (in struct form)  
       __________________________________________________________________________  
         
        References for state equations:  
        1. Marreiros AC, Kiebel SJ, Friston KJ. Dynamic causal modelling for  
           fMRI: a two-state model.  
           Neuroimage. 2008 Jan 1;39(1):269-78.  
         
        2. Stephan KE, Kasper L, Harrison LM, Daunizeau J, den Ouden HE,  
           Breakspear M, Friston KJ. Nonlinear dynamic causal models for fMRI.  
           Neuroimage 42:649-662, 2008.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_fmri_priors.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_fmri_priors", *args, **kwargs)
