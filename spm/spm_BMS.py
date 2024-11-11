from spm.__wrapper__ import Runtime


def spm_BMS(*args, **kwargs):
    """
      Bayesian model selection for group studies  
        FORMAT [alpha,exp_r,xp,pxp,bor] = spm_BMS (lme, Nsamp, do_plot, sampling, ecp, alpha0)  
          
        INPUT:  
        lme      - array of log model evidences   
                     rows: subjects  
                     columns: models (1..Nk)  
        Nsamp    - number of samples used to compute exceedance probabilities  
                   (default: 1e6)  
        do_plot  - 1 to plot p(r|y)  
        sampling - use sampling to compute exact alpha  
        ecp      - 1 to compute exceedance probability  
        alpha0   - [1 x Nk] vector of prior model counts  
          
        OUTPUT:  
        alpha   - vector of model probabilities  
        exp_r   - expectation of the posterior p(r|y)  
        xp      - exceedance probabilities  
        pxp     - protected exceedance probabilities  
        bor     - Bayes Omnibus Risk (probability that model frequencies   
                  are equal)  
          
        REFERENCES:  
         
        Stephan KE, Penny WD, Daunizeau J, Moran RJ, Friston KJ (2009)  
        Bayesian Model Selection for Group Studies. NeuroImage 46:1004-1017  
         
        Rigoux, L, Stephan, KE, Friston, KJ and Daunizeau, J. (2014)  
        Bayesian model selection for group studies - Revisited.   
        NeuroImage 84:971-85. doi: 10.1016/j.neuroimage.2013.08.065  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_BMS.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_BMS", *args, **kwargs)
