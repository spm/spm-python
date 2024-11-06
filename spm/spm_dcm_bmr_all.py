from spm.__wrapper__ import Runtime


def spm_dcm_bmr_all(*args, **kwargs):
    """
      Bayesian model reduction of all permutations of model parameters  
        FORMAT [DCM,BMR,BMA] = spm_dcm_bmr_all(DCM,field,OPT)  
         
        DCM      - A single estimated DCM (or PEB) structure:  
         
         DCM.M.pE  - prior expectation  
         DCM.M.pC  - prior covariance  
         DCM.Ep    - posterior expectation  
         DCM.Cp    - posterior covariances  
         DCM.beta  - prior expectation of reduced parameters (default: 0)  
                     NB: beta  = 'full' uses full prior expectations  
         DCM.gamma - prior variance of reduced parameters (default: 0)  
                     NB:  multiplies the prior variance from the full model  
                     NB2: gamma = 'full' uses full prior variances  
         
        field      - parameter fields in DCM{i}.Ep to optimise [default: {'A','B'}]  
                    'All' will invoke all fields (i.e. random effects)  
                    If Ep is not a structure, all parameters will be considered  
         
        OPT        - Bayesian model selection or averaging: 'BMS' or 'BMA'  
                     [default: 'BMA']  
         
        Returns:  
         
        DCM - Bayesian Model Average (BMA) over models in the final iteration of   
              the search:  
              DCM.M.pE  - reduced prior expectation  
              DCM.M.pC  - reduced prior covariance  
              DCM.Ep    - reduced (BMA/BMS) posterior expectation  
              DCM.Cp    - reduced (BMA/BMS) posterior covariance  
              DCM.Pp    - Model posterior over parameters (with and without)  
         
        BMR -  (Nsub) summary structure reporting the model space from the last  
               iteration of the search:  
         
               BMR.name - character/cell array of parameter names  
               BMR.F    - free energies (relative to full model)  
               BMR.P    - and posterior (model) probabilities  
               BMR.K    - [models x parameters] model space (1 = off, 0 = on)  
         
        BMA - Baysian model average (over reduced models; see spm_dcm_bma)  
         
       --------------------------------------------------------------------------  
        This routine searches over reduced (nested) models of a full model (DCM)   
        using Bayesian model reduction and performs Bayesian Model Averaging.  
        'Reduced' means some free parameters (parameters with a non-  
        zero prior covariance) are switched off by fixing their prior variance   
        to zero.   
         
        If there are fewer than nmax = 8 free parameters, all permutations of   
        switching off parameters will be tested. Otherwise, this routine   
        implements the following greedy search procedure. The nmax parameters   
        are identified which, when switched off individually, produce the least   
        reduction (greatest increase) in model evidence. All permutations of   
        switching off these parameters are then evaluated and the best   
        permutation is retained. This procedure is repeated until all nmax  
        parameters are retained or there are no more parameters to consider.   
        Finally, BMA is performed on the models from the last iteration.  
          
        NB: The full model should be estimated prior to running this function. A  
        summary of the reduced model is plotted when the number of output  
        arguments is greater than one.  
         
        See also: spm_dcm_post_hoc - this routine is essentially a simplified  
        version of spm_dcm_post_hoc  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_bmr_all.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_bmr_all", *args, **kwargs)
