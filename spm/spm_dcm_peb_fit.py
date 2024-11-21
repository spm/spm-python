from spm.__wrapper__ import Runtime


def spm_dcm_peb_fit(*args, **kwargs):
    """
      Bayesian group inversion using empirical Bayes  
        FORMAT [DCM,PEB,M] = spm_dcm_peb_fit(DCM,M,field)  
         
        DCM    - {N [x M]} structure array of DCMs from N subjects  
        ------------------------------------------------------------  
            DCM{i}.M.pE - prior expectation of parameters  
            DCM{i}.M.pC - prior covariances of parameters  
            DCM{i}.Ep   - posterior expectations  
            DCM{i}.Cp   - posterior covariance  
            DCM{i}.FEB  - free energy over empirical Bayes iterations  
            DCM{i}.EEB  - second level log-precisions over iterations  
            DCM{i}.HEB  - conditional entropy (uncertainty) over iterations  
         
        M.X    - second level design matrix, where X(:,1) = ones(N,1) [default]  
        M.pE   - second level prior expectation of parameters  
        M.pC   - second level prior covariances of parameters  
        M.hE   - second level prior expectation of log precisions  
        M.hC   - second level prior covariances of log precisions  
         
        field  - parameter fields in DCM{i}.Ep to optimise [default: {'A','B'}]  
                 'All' will invoke all fields (i.e. random effects)  
         
         
        DCM  - DCM structures inverted with emprical priors  
        PEB  - second level model structure  
        F    - ssecond level free energy over iterations  
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
         
       --------------------------------------------------------------------------  
        This routine performs hierarchical empirical Bayesian inversion of a  
        group DCM study. It uses Bayesian model reduction to place second  
        (between subject) level constraints on the coordinate descent implicit  
        in the inversion of DCMs at the first (within subject) level. In other  
        words, at each iteration (or small number of iterations) of the within  
        subject inversion, the priors are updated using empirical priors from  
        the second level. The free energy of this hierarchical model comprises  
        the complexity of group effects plus the sum of free energies from each  
        subject - evaluated under the empirical priors  provided by the second  
        level.  
         
        If called with a cell array, each column is assumed to contain the same  
        model of a different subject or dataset, while each row contains  
        different models of the same dataset. Bayesian model reduction will be  
        applied automatically, after inversion of the full model, which is  
        assumed to occupy the first column.  
         
        The posterior densities of subject or session specific DCMs are adjusted  
        so that they correspond to what would have been obtained under the  
        original priors. Effectively, this group inversion is used to suppress  
        local minima, prior to inference on group means.  
         
        see also: spm_dcm_fit.m; spm_dcm_peb.m; spm_dcm_bmr.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_peb_fit.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_peb_fit", *args, **kwargs)
