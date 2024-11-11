from spm.__wrapper__ import Runtime


def spm_dcm_peb_rnd(*args, **kwargs):
    """
      Re-randomisation testing for empirical Bayes and DCM  
        FORMAT [p,P,f,F,X] = spm_dcm_peb_rnd(DCM,M,field)  
         
        DCM   - {N x 1} structure DCM array of (M) DCMs from (N) subjects  
        -------------------------------------------------------------------  
            DCM{i}.M.pE - prior expectation of parameters  
            DCM{i}.M.pC - prior covariances of parameters  
            DCM{i}.Ep   - posterior expectations  
            DCM{i}.Cp   - posterior covariance  
         
        M.X    - second level design matrix, where X(:,1) = ones(N,1) [default]  
        M.pE   - second level prior expectation of parameters  
        M.pC   - second level prior covariances of parameters  
        M.hE   - second level prior expectation of log precisions  
        M.hC   - second level prior covariances of log precisions  
        M.Q    - covariance components: {'single','fields','all','none'}  
         
        M.N    -  number of re-randomizations [default: M.N = 32]  
         
        field  - parameter fields in DCM{i}.Ep to optimise [default: {'A','B'}]  
                 'All' will invoke all fields  
          
        p      - classical (re-randomization) p-value  
        P      - null distribution of p-values  
        f      - Bayesian (posterior) p-value  
        F      - null distribution of log Bayes factors  
        X      - randomised design generating non-distribution  
       __________________________________________________________________________  
         
        This routine uses the posterior  density over the coefficients of between  
        subject effects encoded by a design matrix X. It is assumed that the  
        second column of X contains classification or predictor variables. The  
        significance of group effects is assessed using re-randomization by  
        permuting the element s(of the second) explanatory variable. This  
        provides a null distribution for the relative free energy and a posterior  
        probability over random permutations of the second level model.  
         
        See also: spm_dcm_peb.m and spm_dcm_loo.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_peb_rnd.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_peb_rnd", *args, **kwargs)
