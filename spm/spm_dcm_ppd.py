from spm.__wrapper__ import Runtime


def spm_dcm_ppd(*args, **kwargs):
    """
      Posterior predictive density for empirical Bayes and DCM  
        FORMAT [qE,qC,P] = spm_dcm_ppd(TEST,TRAIN,Y,X,field,i)  
         
        TEST   - {1 [x M]} structure DCM array of new subject  
        TRAIN  - {N [x M]} structure DCM array of (M) DCMs from (N) subjects  
        --------------------------------------------------------------------  
            DCM{i}.M.pE - prior expectation of parameters  
            DCM{i}.M.pC - prior covariances of parameters  
            DCM{i}.Ep   - posterior expectations  
            DCM{i}.Cp   - posterior covariance  
         
        Y      - known values of design (i.e., GLM) matrix for the test subject  
        X      - second level design matrix, where X(:,1) = ones(N,1) [default]  
        field  - parameter fields in DCM{i}.Ep to optimise [default: {'A','B'}]  
                 'All' will invoke all fields (these constitute random effects)  
        iX     - column of design matrix to be predicted [default: iX=2]  
          
        qE     - posterior predictive expectation  
        qC     - posterior predictive covariances  
        P      - posterior probability over unique values of X(:,2)  
       __________________________________________________________________________  
         
        This routine inverts a hierarchical DCM using variational Laplace and  
        Bayesian model reduction. In essence, it optimises the empirical priors  
        over the parameters of a training set of first level DCMs, using between  
        subject constraints specified in the design matrix X. These optimised  
        empirical priors are then used to parameterise a model of between subject  
        effects for a single (test) subject. Usually, the second level of the  
        design matrix specifies group differences and the posterior predictive  
        density over this group effect can be used for classification or cross  
        validation. it is assumed that the unknown predictive (i.e., explanatory  
        variable in the design matrix pertains to the second column unless  
        otherwise specified by iX  
         
        See also: spm_dcm_peb.m and spm_dcm_loo.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_ppd.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_ppd", *args, **kwargs)
