from spm.__wrapper__ import Runtime


def spm_BMS_F(*args, **kwargs):
    """
      Compute two lower bounds on model evidence p(y|r) for group BMS  
        FORMAT [F_samp,F_bound] = spm_BMS_F(alpha,lme,alpha0)  
          
        alpha    - parameters of p(r|y)  
        lme      - array of log model evidences   
                     rows:    subjects  
                     columns: models (1..Nk)  
        alpha0   - priors of p(r)  
          
        F_samp   - sampling estimate of <ln p(y_n|r)>  
        F_bound  - lower bound on lower bound of <ln p(y_n|r)>  
          
        Reference:  
        Stephan KE, Penny WD, Daunizeau J, Moran RJ, Friston KJ  
        Bayesian Model Selection for Group Studies. Neuroimage 2009 46(4):1004-17  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_BMS_F.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_BMS_F", *args, **kwargs)
