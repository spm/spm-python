from spm.__wrapper__ import Runtime


def spm_dcm_peb_full(*args, **kwargs):
    """
      Hierarchical (PEB) inversion of DCMs using BMR and VL  
        FORMAT [PEB,DCM] = spm_dcm_peb_full(DCM,M,field)  
        FORMAT [PEB,DCM] = spm_dcm_peb_full(DCM,X,field)  
         
        DCM    - {N [x M]} structure array of DCMs from N subjects  
        ------------------------------------------------------------  
            DCM{i}.M.pE - prior expectation of parameters  
            DCM{i}.M.pC - prior covariances of parameters  
            DCM{i}.Ep   - posterior expectations  
            DCM{i}.Cp   - posterior covariance  
         
        M.X    - second level design matrix, where X(:,1) = ones(N,1) [default]  
        M.pE   - second level prior expectation of parameters  
        M.pC   - second level prior covariances of parameters  
        M.hE   - second level prior expectation of log precisions  
        M.hC   - second level prior covariances of log precisions  
          
        field  - parameter fields in DCM{i}.Ep to optimise [default: {'A','B'}]  
                 'All' will invoke all fields. this argument effectively allows   
                 one to specify which parameters constitute random effects.       
          
        PEB    - hierarchical dynamic model  
        -------------------------------------------------------------  
            PEB.Snames - string array of first level model names  
            PEB.Pnames - string array of parameters of interest  
            PEB.Pind   - indices of parameters in spm_vec(DCM{i}.Ep)   
          
            PEB.M.X  -   second level (between subject) design matrix  
            PEB.M.W  -   second level (within  subject) design matrix  
            PEB.M.Q  -   precision [components] of second level random effects   
            PEB.M.pE -   prior expectation of second level parameters  
            PEB.M.pC -   prior covariance  of second level parameters  
            PEB.M.hE -   prior expectation of second level log-precisions  
            PEB.M.hC -   prior covariance  of second level log-precisions  
            PEB.Ep   -   posterior expectation of second level parameters  
            PEB.Eh   -   posterior expectation of second level log-precisions  
            PEB.Cp   -   posterior covariance  of second level parameters  
            PEB.Ch   -   posterior covariance  of second level log-precisions  
            PEB.Ce   -   expected covariance of second level random effects  
            PEB.F    -   free energy of second level model  
         
        DCM    - 1st level (reduced) DCM structures with emprical priors  
         
                 If DCM is an an (N x M} array, hierarchicial inversion will be  
                 applied to each model (i.e., each row) - and PEB will be a   
                 {1 x M} cell array.  
         
       --------------------------------------------------------------------------  
        This routine inverts a hierarchical DCM using variational Laplace and  
        Bayesian model reduction. In essence, it optimises the empirical priors  
        over the parameters of a set of first level DCMs, using  second level or  
        between subject constraints specified in the design matrix X. This scheme  
        is efficient in the sense that it does not require inversion of the first  
        level DCMs - it just requires the prior and posterior densities from each  
        first level DCMs to compute empirical priors under the implicit  
        hierarchical model. The output of this scheme (PEB) can be re-entered  
        recursively to invert deep hierarchical models. Furthermore, Bayesian  
        model comparison (BMC) can be specified in terms of the empirical  
        priors to perform BMC at the group level. Alternatively, subject-specific  
        (first level) posterior expectations can be used for classical inference  
        in the usual way. Note that these (summary statistics) and  optimal in  
        the sense that they have been estimated under empirical (hierarchical)   
        priors.  
         
        If called with a single DCM, there are no between subject effects and the  
        design matrix is assumed to model mixtures of parameters at the first  
        level.  
         
        If called with a cell array, each column is assumed to contain 1st level  
        DCMs inverted under the same model.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_peb_full.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_peb_full", *args, **kwargs)
