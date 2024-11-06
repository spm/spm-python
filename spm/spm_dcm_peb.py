from spm.__wrapper__ import Runtime


def spm_dcm_peb(*args, **kwargs):
    """
      Hierarchical (PEB) inversion of DCMs using BMR and VL  
        FORMAT [PEB,DCM] = spm_dcm_peb(DCM,M,field)  
        FORMAT [PEB,DCM] = spm_dcm_peb(DCM,X,field)  
         
        DCM    - {N [x M]} structure array of DCMs from N subjects  
        -------------------------------------------------------------------------  
            DCM{i}.M.pE   - prior expectation of parameters  
            DCM{i}.M.pC   - prior covariances of parameters  
            DCM{i}.Ep     - posterior expectations  
            DCM{i}.Cp     - posterior covariance  
            DCM{i}.F      - free energy  
         
        M.X      - 2nd-level design matrix (between subject): X(:,1) = ones(N,1) [default]  
        M.W      - 2nd-level design matrix (within subject) [default eye(n,n)]  
        M.bE     - 3rd-level prior expectation [default: DCM{1}.M.pE]  
        M.bC     - 3rd-level prior covariance  [default: DCM{1}.M.pC/M.alpha]  
        M.pC     - 2nd-level prior covariance  [default: DCM{1}.M.pC/M.beta]  
        M.hE     - 2nd-level prior expectation of log precisions [default: 0]  
        M.hC     - 2nd-level prior covariances of log precisions [default: 1/16]  
        M.maxit  - maximum iterations [default: 64]  
        M.noplot - if this field exists then text output will be suppressed  
         
        M.Q      - covariance components: {'single','fields','all','none'}  
        M.alpha  - optional scaling to specify M.bC [default = 1]  
        M.beta   - optional scaling to specify M.pC [default = 16]  
                 - if beta equals 0, sample variances will be used  
         
        NB: the prior covariance of 2nd-level random effects is:  
                   exp(M.hE)*DCM{1}.M.pC/M.beta [default DCM{1}.M.pC/16]  
         
        NB2:       to manually specify which parameters should be assigned to   
                   which covariance components, M.Q can be set to a cell array of   
                   [nxn] binary matrices, where n is the number of DCM   
                   parameters. A value of M.Q{i}(n,n) = 1 means that parameter   
                   n should be modelled with component i.  
         
        M.Xnames - cell array of names for second level parameters [default: {}]  
          
        field    - parameter fields in DCM{i}.Ep to optimise [default: {'A','B'}]  
                   'all' will invoke all fields. This argument effectively allows   
                   one to specify the parameters that constitute random effects.       
          
        PEB      - hierarchical dynamic model  
        -------------------------------------------------------------------------  
            PEB.Snames    - string array of first level model names  
            PEB.Pnames    - string array of parameters of interest  
            PEB.Pind      - indices of parameters at the level below  
            PEB.Pind0     - indices of parameters in spm_vec(DCM{i}.Ep)   
            PEB.Xnames    - names of second level parameters  
          
            PEB.M.X       - second level (between-subject) design matrix  
            PEB.M.W       - second level (within-subject) design matrix  
            PEB.M.Q       - precision [components] of second level random effects   
            PEB.M.pE      - prior expectation of second level parameters  
            PEB.M.pC      - prior covariance of second level parameters  
            PEB.M.hE      - prior expectation of second level log-precisions  
            PEB.M.hC      - prior covariance of second level log-precisions  
            PEB.Ep        - posterior expectation of second level parameters  
            PEB.Eh        - posterior expectation of second level log-precisions  
            PEB.Cp        - posterior covariance of second level parameters  
            PEB.Ch        - posterior covariance of second level log-precisions  
            PEB.Ce        - expected  covariance of second level random effects  
            PEB.F         - free energy of second level model  
         
        DCM       - 1st level (reduced) DCM structures with empirical priors  
         
                 If DCM is an an (N x M} array, hierarchical inversion will be  
                 applied to each model (i.e., each row) - and PEB will be a   
                 {1 x M} cell array.  
          
        This routine inverts a hierarchical DCM using variational Laplace and  
        Bayesian model reduction. In essence, it optimises the empirical priors  
        over the parameters of a set of first level DCMs, using second level or  
        between subject constraints, specified in the design matrix X. This scheme  
        is efficient in the sense that it does not require inversion of the first  
        level DCMs - it just requires the prior and posterior densities from each  
        first level DCM to compute empirical priors under the implicit  
        hierarchical model. The output of this scheme (PEB) can be re-entered  
        recursively to invert deep hierarchical models. Furthermore, Bayesian  
        model comparison (BMC) can be specified in terms of the empirical priors  
        to perform BMC at the group level. Alternatively, subject-specific (first  
        level) posterior expectations can be used for classical inference in the  
        usual way. Note that these (summary statistics) are optimal in the sense  
        that they have been estimated under empirical (hierarchical)  priors.  
         
        If called with a single subject (or DCM), there are no between subject  
        effects and the second level GLM simply modelsmixtures of parameters at  
        the first level. These mixtures are specified by M.W, where M.X = 1. When  
        called with multiple subjects (or DCMs)it is assumed that all parameters  
        specified by the input argument 'field' are explained by the same between  
        subject effects in M.X. This means that M.W becomes an identity matrix,  
        such that the implicit GLM over subjects and parameters is kron(X,W).  
         
        If called with a cell array, each column is assumed to contain 1st  
        level DCMs inverted under the same model.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_peb.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_peb", *args, **kwargs)
