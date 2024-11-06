from spm.__wrapper__ import Runtime


def spm_dcm_fnirs_priors(*args, **kwargs):
    """
      Priors for a one-state DCM for fNIRS  
        FORMAT [pE,pC,x] = spm_dcm_fnirs_priors(DCM)  
         
        INPUT:  
           DCM.a,DCM.b,DCM.c,DCM.c - constraints on connections (1 - present, 0 - absent)  
           DCM.n - number of sources of interest   
           DCM.Y.nch - number of channels of interest   
           DCM.options.two_state:  (0 or 1) one or two states per region  
           DCM.options.stochastic: (0 or 1) exogenous or endogenous fluctuations  
           DCM.options.precision:           log precision on connection rates  
         
        OUTPUT:  
           pE     - prior expectations (connections and hemodynamic)  
           pC     - prior covariances  (connections and hemodynamic)  
           x      - prior (initial) states  
       __________________________________________________________________________  
         
        References for state equations:  
        1. Marreiros AC, Kiebel SJ, Friston KJ. Dynamic causal modelling for  
           fMRI: a two-state model.  
           Neuroimage. 2008 Jan 1;39(1):269-78.  
         
        2. Stephan KE, Kasper L, Harrison LM, Daunizeau J, den Ouden HE,  
           Breakspear M, Friston KJ. Nonlinear dynamic causal models for fMRI.  
           Neuroimage 42:649-662, 2008.  
         
        3. Tak S, Kempny AM, Friston, KJ, Leff, AP, Penny WD. Dynamic causal  
           modelling for functional near-infrared spectroscopy.   
           Neuroimage 111: 338-349, 2015.   
         
        This script is based on spm_dcm_fmri_priors.m written by Karl Friston.  
          
        In this script, optics priors are added, prior covariance of A is changed,   
        prior for extended Balloon model (viscoelastic time constant) is added.   
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_fnirs/spm_dcm_fnirs_priors.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_fnirs_priors", *args, **kwargs)
