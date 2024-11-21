from spm.__wrapper__ import Runtime


def spm_dcm_peb_bmc(*args, **kwargs):
    """
      Hierarchical (PEB) model comparison and averaging (2nd level)  
        FORMAT [BMA] = spm_dcm_peb_bmc(PEB,models)  
        FORMAT [BMA] = spm_dcm_peb_bmc(PEB)  
         
        PEB -  between subject (second level) effects (from spm_dcm_peb)  
        ------------------------------------------------------------  
            PEB.Snames - string array of Ns first level model names  
            PEB.Pnames - string array of Np parameters of interest  
         
            PEB.M.X  -   second level (between subject) design matrix  
            PEB.M.W  -   second level (within  subject) design matrix  
            PEB.M.Q  -   precision components of second level random effects  
            PEB.M.pE -   prior expectation of second level parameters  
            PEB.M.pC -   prior covariance  of second level parameters  
            PEB.Ep   -   posterior expectation of second level parameters  
            PEB.Cp   -   posterior covariance  of second level parameters  
         
        models - field in DCM.Ep to compare For the first two group effects  
                 or logical (Nm x Np) matrix of Nm (parametric) model space  
                 or an array of DCMs specifying Nm (parametric) model space  
         
        if models are not specified, all combinations of second level parameters  
        will be tested.  
         
        fields - (optional) for use with pre-defined model spaces only. Limits   
                 the parameters that vary across models to those with names   
                 matching those provided. All excluded parameters are switched  
                 on in all models. Cell array of chars.  
         
        BMA    - DCM structure of Bayesian model average  
        -------------------------------------------------------------------------  
            BMA.Snames - string array of first level model names  
            BMA.Pnames - string array of parameters of interest  
         
            BMA.Ep   - BMA expectation of second level parameters  
            BMA.Cp   - BMA   variances of second level parameters  
            BMA.M    - second level model  
         
            BMA.F    - free energy over model space  
            BMA.P    - posterior probability over models  
            BMA.Px   - posterior probability over parameters (differences)  
            BMA.Pw   - posterior probability over parameters (common)  
         
            BMA.K     - [models x parameters] model space (0 = off, 1 = on)  
            BMA.Kind  - indices of DCM parameters which varied across models  
            BMA.Kname - names of DCM parameters which varied across models  
         
        or for automatic model search, see spm_dcm_bmr_all.m (output: DCM)  
         
        BMR   - Parameters and evidence of reduced models which produced the BMA  
        -------------------------------------------------------------------------  
            BMR{i,j}    - model i of commonalities and j of group differences  
            BMR{i,j}.Ep - expectations of second level parameters  
            BMR{i,j}.Cp - covariance of second level parameters  
            BMR{i,j}.F  - free energy relative to full model  
         
        or for automatic model search:  
         
            BMR.name   - parameter names  
            BMR.F      - free energy relative to full model  
            BMR.P      - and posterior (model) probabilities  
            BMR.K      - [models x parameters] model space (1 = off, 2 = on)  
         
       --------------------------------------------------------------------------  
        This routine performs Bayesian model comparison and averaging of second  
        level or hierarchical (PEB) models. The model space is defined either  
        in terms of fields (e.g. 'A' or 'B') or as a logical matrix, with one row  
        per model and a column per parameter (in PEB.Pnames). This induces  
        a joint model space over parameters and group effects at the second level  
        (encoded by the design matrix, X). Using Bayesian model reduction, this  
        joint model space is scored over the specified models at the first level  
        (for the constant terms modelling effects that are common to all  
        subjects) and combinations of group effects (modelling between  
        subject differences).  
         
        If there is only a group effect (and no between subject differences) this  
        reduces to a search over different models of the group mean.  
         
        Given the model space one can then compute the posterior probability  
        of various combinations of group effects over different parameters. Of  
        particular interest are (i) the posterior probabilities over the  
        the first two group effects in the design matrix and the posterior  
        probability of models with and without each parameter, for the common  
        (first) and subject-specific (second) group affects (returned in BMA.P,  
        BMA.Pw and BMA.Px respectively. The Bayesian model averages of the second  
        level parameters and can be found in BMA.Ep and BMA.Cp.  
         
        If models are not specified, all combinations of individual  
        parameters over all group effects will be considered and the ensuing  
        Bayesian model reduction reported for each effect in the design matrix.  
         
        NB for EEG models the absence of a connection means it is equal to its  
        prior mesn, not that is is zero.  
         
        see also: spm_dcm_peb.m and spm_dcm_bmr  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_peb_bmc.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_peb_bmc", *args, **kwargs)
