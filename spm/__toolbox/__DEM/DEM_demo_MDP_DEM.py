from spm.__wrapper__ import Runtime


def DEM_demo_MDP_DEM(*args, **kwargs):
    """
      Demo of mixed continuous and discrete state space modelling  
       __________________________________________________________________________  
         
        This routine  illustrates the combination of discrete and continuous  
        state space models for active inference. In this example, the lowest  
        level of a hierarchical Markov decision process (used to illustrate  
        evidence accumulation during reading in related simulations) is equipped  
        with a continuous time and state space dynamical model at the lowest  
        level. This allows one to model both the categorical belief updates  
        using belief propagation and the continuous belief updates using  
        Bayesian filtering within the same model and associated inversion  
        scheme.  
         
        The key contribution of this  scheme is the message passing or belief  
        propagation between the lowest discrete state (MDP) level and the  
        highest level of the continuous state (DCM) models. In brief, during  
        inversion, posterior beliefs about hidden causes of observable  
        (continuous) inputs provide (probabilistic or posterior) outcomes for the  
        (categorical) MDP scheme. In return, the posterior predictive density  
        over outcomes of the MDP scheme specify priors on the hidden causes. In  
        this example, these priors determine the salient locations to which the  
        synthetic agent saccades. These saccades sample discriminative visual  
        information that resolves uncertainty about the content of the local  
        visual scene. Posterior expectations about the content then play the role  
        of observations for higher (categorical) levels.  
         
        Note that the priors from the MDP levels are time invariant (i.e., the  
        attracting location of the saccade does not change during each saccadic  
        epoch). Similarly, the posterior beliefs are over attributes that do  
        not change during the saccadic sampling (i.e., the hidden cause of  
        visual input at the attracting location). This underwrites a separation  
        of temporal scales that is recapitulated at higher levels of the  
        categorical model. The implementation of these schemes is as general as  
        we could make it. The code below illustrates how one links MDP schemes  
        to DPM schemes in a generic way through  hidden causes.  
         
        More details about each level of the model are provided in line as  
        annotated descriptions.  
         
        see also: spm_MPD_VB_X.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_MDP_DEM.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_MDP_DEM", *args, **kwargs)
