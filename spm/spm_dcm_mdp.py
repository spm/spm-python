from spm.__wrapper__ import Runtime


def spm_dcm_mdp(*args, **kwargs):
    """
      MDP inversion using Variational Bayes  
        FORMAT [DCM] = spm_dcm_mdp(DCM)  
         
        Expects:  
       --------------------------------------------------------------------------  
        DCM.MDP   % MDP structure specifying a generative model  
        DCM.field % parameter (field) names to optimise  
        DCM.U     % cell array of outcomes (stimuli)  
        DCM.Y     % cell array of responses (action)  
         
        Returns:  
       --------------------------------------------------------------------------  
        DCM.M     % generative model (DCM)  
        DCM.Ep    % Conditional means (structure)  
        DCM.Cp    % Conditional covariances  
        DCM.F     % (negative) Free-energy bound on log evidence  
          
        This routine inverts (cell arrays of) trials specified in terms of the  
        stimuli or outcomes and subsequent choices or responses. It first  
        computes the prior expectations (and covariances) of the free parameters  
        specified by DCM.field. These parameters are log scaling parameters that  
        are applied to the fields of DCM.MDP.   
         
        If there is no learning implicit in multi-trial games, only unique trials  
        (as specified by the stimuli), are used to generate (subjective)  
        posteriors over choice or action. Otherwise, all trials are used in the  
        order specified. The ensuing posterior probabilities over choices are  
        used with the specified choices or actions to evaluate their log  
        probability. This is used to optimise the MDP (hyper) parameters in  
        DCM.field using variational Laplace (with numerical evaluation of the  
        curvature).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_mdp.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_mdp", *args, **kwargs)
