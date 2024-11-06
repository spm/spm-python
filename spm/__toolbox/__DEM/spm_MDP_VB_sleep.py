from spm.__wrapper__ import Runtime


def spm_MDP_VB_sleep(*args, **kwargs):
    """
      Bayesian model reduction (sleep) for MDP models  
        FORMAT [MDP] = spm_MDP_VB_sleep(MDP,BMR)  
         
        MDP  - (inverted) MDP structure  
         
        BMR.g - modality [default: 1]  
        BMR.o - outcomes - that induce REM [default: {}]  
        BMR.x - increase in concentration parameters for BMR [default: 8]  
        BMR.f - hidden factors to contract over [default: 0]  
        BMR.T - log Bayes factor threshold [default: 2]  
         
        MDP  - (reduced) model structure: with reduced MDP.a  
         
        This routine optimises the hyperparameters of a POMDP model (i.e.,  
        concentration parameters encoding likelihoods). It uses Bayesian model  
        reduction to evaluate the evidence for models with and without changes  
        in Dirichlet counts (c.f., SWS or introspection)  
         
        If specified, the scheme will then recompute posterior beliefs about the  
        model parameters based upon (fictive) outcomes generated under its  
        (reduced) generative model.(c.f., REM sleep)  
         
        This version compares models (i.e., prior concentration parameters) that  
        change in the direction of maximising expected free energy; namely,  
        maximising the mutual information entailed by a likelihood mapping or  
        transition matrix (plus the log preference over outcomes or states). If  
        the reduced prior exceeds the specified Occams window, in terms of the  
        reduced free energy, the reduced  priors and posteriors replace the full  
        priors and posteriors. Effectively, this implements the structural  
        hyperprior that likelihood mappings with a high mutual information are  
        plausible and accepts these new priors if there is sufficient evidence  
        for them. This can be regarded as a generic form of structure learning.  
         
        See also: spm_MDP_log_evidence.m, spm_MDP_VB and spm_MDP_VB_update.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_MDP_VB_sleep.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_MDP_VB_sleep", *args, **kwargs)
