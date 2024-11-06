from spm.__wrapper__ import Runtime


def spm_dcm_loo(*args, **kwargs):
    """
      Leave-one-out cross-validation for empirical Bayes and DCM  
        FORMAT [qE,qC,Q] = spm_dcm_loo(DCM,M,field)  
         
        DCM   - {N [x M]} structure DCM array of (M) DCMs from (N) subjects  
        -------------------------------------------------------------------  
            DCM{i}.M.pE   - prior expectation of parameters  
            DCM{i}.M.pC   - prior covariances of parameters  
            DCM{i}.Ep     - posterior expectations  
            DCM{i}.Cp     - posterior covariance  
         
        M.X       - second level design matrix, where X(:,1) = ones(N,1) [default]  
        field     - parameter fields in DCM{i}.Ep to optimise [default: {'A','B'}]  
                    'All' will invoke all fields  
          
        qE        - posterior predictive expectation (group effect)  
        qC        - posterior predictive covariances (group effect)  
        Q         - posterior probability over unique levels of X(:,2)  
          
        This routine uses the posterior predictive density over the coefficients  
        of between-subject effects encoded by a design matrix X. It is assumed  
        that the second column of X contains classification or predictor  
        variables. A cross-validation scheme is used to estimate the mixture of  
        parameters at the first (within-subject) level that are conserved over  
        subjects in terms of a constant (first column of X) and differences  
        (second column of X). Using a leave-one-out scheme, the predictive  
        posterior density of the predictive variable is used to assess  
        cross-validation accuracy. For multiple models, this procedure is  
        repeated for each model in the columns of the DCM array.  
          
        See also: spm_dcm_peb.m and spm_dcm_ppd.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_loo.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_loo", *args, **kwargs)
