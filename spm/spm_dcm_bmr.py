from spm.__wrapper__ import Runtime


def spm_dcm_bmr(*args, **kwargs):
    """
      Bayesian model reduction (under Laplace approximation)  
        FORMAT [RCM,BMC,BMA] = spm_dcm_bmr(P,[field])  
         
        P     - {Nsub x Nmodel} cell array of DCM filenames or model structures    
                of Nsub subjects, where each model is reduced independently   
         
        field - parameter fields in DCM{i}.Ep to plot, or the fields to search   
                if only one DCM is provided per subject [default: {'A','B'}]  
               
        RCM   - reduced DCM array  
        BMC   - (Nsub) summary structure   
                 BMC.name - character/cell array of DCM filenames  
                 BMC.F    - their associated free energies  
                 BMC.P    - and posterior (model) probabilities  
        BMA   - Baysian model average (see spm_dcm_bma)  
       __________________________________________________________________________  
          
        spm_dcm_bmr operates on different DCMs of the same data (rows) to find  
        the best model. It assumes the full model - whose free-parameters are  
        the union (superset) of all free parameters in each model - has been  
        inverted. A post hoc selection procedure is used to evaluate the log-  
        evidence and conditional density over free-parameters of each model  
        specified.  
         
        Reduced models can be specified either in terms of the allowable  
        connections (specified in the DCM.A/a, DCM.B/b and DCM.C/c fields) or the  
        resulting prior density (specified in DCM.pE and DCM.pC).  If the  
        latter exist, they will be used as the model specification.  
         
        If a single subject (DCM) is specified, an exhaustive search will  
        be performed.  
         
        The outputs of this routine are graphics reporting the model space search  
        (optimisation) and the reduced (cell array of) DCM structures.  
         
        See also: spm_dcm_post_hoc.m, spm_dcm_bpa, spm_dcm_peb and spm_dcm_bma  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_bmr.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_bmr", *args, **kwargs)
