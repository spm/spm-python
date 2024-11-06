from spm.__wrapper__ import Runtime


def spm_dcm_bmc_peb(*args, **kwargs):
    """
      Hierarchical (PEB) model comparison and averaging (1st and 2nd level)  
        FORMAT [BMC,PEB] = spm_dcm_bmc_peb(DCM,[M,field])  
         
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
                 'All' will invoke all fields (i.e. random effects)  
         
        BMC    - Bayesian model comparison structure   
        -------------------------------------------------------------  
            BMC.F    - free energy over joint model space  
            BMC.P    - posterior probability over models  
            BMC.Px   - posterior probability over 1st level models  
            BMC.Pw   - posterior probability over 2nd level models  
            BMC.M    - second level model  
            BMC.K    - model space  
         
        PEB    - selected (best) second level model and parameter estimates  
        -------------------------------------------------------------  
            PEB.Snames - string array of first level model names  
            PEB.Pnames - string array of parameters of interest  
            PEB.Pind   - indices of parameters in spm_vec(DCM{i}.Ep)   
         
            PEB.M    -   first level (within subject) model  
            PEB.Ep   -   posterior expectation of second level parameters  
            PEB.Eh   -   posterior expectation of second level log-precisions  
            PEB.Cp   -   posterior covariance  of second level parameters  
            PEB.Ch   -   posterior covariance  of second level log-precisions  
            PEB.Ce   -   expected covariance of second level random effects  
            PEB.F    -   free energy of second level model  
         
       --------------------------------------------------------------------------  
        This routine performs Bayesian model comparison in the joint space of  
        models specified in terms of (first level) model parameters and models  
        specified in terms of (second level) group effects. The first level model  
        space is defined by the columns of the DCM array, while the second level  
        model space is specified by combinations of second level effects encoded   
        in a design matrix.  The first effect in the design matrix is assumed   
        to be a constant term that models a group mean.  
         
        This routine assumes that all the models have been reduced (i.e. inverted  
        using Bayesian model reduction). It then use sempirical Bayes and the  
        summary statistic approach to evaluate the relative contributions of  
        between subject effects by considering all combinations of columns in the  
        design matrix.  
         
        This Bayesian model comparison should be contrasted with model  
        comparison at the second level. Here, we are interested in the best model  
        of first level parameters that show a second level effect. This is not  
        the same as trying to find the best model of second level effects. Model  
        comparison among second level parameters uses spm_dcm_peb_bmc.  
         
        NB for EEG models the absence of a connection means it is equal to its  
        prior mesn, not that is is zero.  
         
        see also: spm_dcm_peb.m and spm_dcm_bmr_peb  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_bmc_peb.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_bmc_peb", *args, **kwargs)
