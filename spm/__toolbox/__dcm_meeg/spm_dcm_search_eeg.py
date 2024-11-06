from spm.__wrapper__ import Runtime


def spm_dcm_search_eeg(*args, **kwargs):
    """
      Bayesian model reduction (under Laplace approximation)  
        FORMAT [DCM,RCM] = spm_dcm_search_eeg(P,SAVE_DCM)  
         
        P - {Nsub x Nmodel} cell array of DCM filenames or model structures for   
             Nsub subjects, where each model is reduced independently for each  
             subject  
               
        SAVE_DCM - optional flag to save DCMs  
          
        DCM - reduced (best) DCM  
        RCM - reduced DCM array  
         
        Each reduced model requires DCM.A,DCM.B,DCM.C and DCM.options.model  
        or the implicit prior expectation and covariances in DCM.pE and DCM.pC  
        if the reduce models are specified explicitly in terms of prior  
        expectations and covariances (pE and pC) these will be used first.  
         
       --------------------------------------------------------------------------  
        spm_dcm_search_eeg operates on different DCMs of the same data to find  
        the best model. It assumes the full model - whose free-parameters are  
        the union (superset) of all free parameters in each model - has been  
        inverted. A post hoc selection procedure is used to evaluate the log-  
        evidence and conditional density over free-parameters of each model  
        specified.  
         
        Reduced models can be specified either in terms of the allowable  
        connections (specified in the DCM.A, DCM.B and DCM.C fields) or the  
        resulting prior density (specified in DCM.pE and DCM.pC).  If the  
        latter exist, they will be used as the model specification.  
         
        The outputs of this routine are graphics reporting the model space search  
        (optimisation) and a DCM_optimum (in the first DCMs directory) for the  
        best DCM. The structural and function (spectral embedding) graphs are  
        based on this DCM.  
         
        Conditional esimates (Ep, Cp and F values) in DCM_??? (specifed by P) are  
        replaced by their reduced estimates (but only these estimates) in rDCM_???  
         
        DCM_optimum (saved with nargout = 0) contains the fields:  
         
               DCM.Pname - character/cell array of DCM filenames  
               DCM.PF    - their associated free energies  
               DCM.PP    - and posterior (model) probabilities  
         
        If requested, the free energies and posterior estimates of each DCM in P  
        are saved for subsequent searches over different partitions of model  
        space.  
         
        See also: spm_dcm_post_hoc.m, spm_dcm_group and spm_dcm_bma  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_search_eeg.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_search_eeg", *args, **kwargs)
