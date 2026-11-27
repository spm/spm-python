from spm._runtime import Runtime


def DEM_reasoning(*args, **kwargs):
    r"""
      Demo of active inference for visual salience  
       __________________________________________________________________________  
        This routine illustrates active reasoning; namely, choosing policies that  
        disambiguate among prior beliefs about hypotheses or model structure. In  
        this example, the hypotheses concern the likelihood mapping between  
        latent causes and a particular outcome modality (correct or not). The  
        example used to demonstrate this form of active model selection revisits  
        the three-ball paradigm, in which the correct colour is the colour of a  
        ball in a location signified by the colour of another ball. In other  
        words, this is a minimal setup or puzzle that features an unknown rule,  
        invariance, equivariance or symmetry. In this case, a rule is taken to  
        mean the equivalence between a control and stayed that depends upon a  
        context state. Here, the context is specified by the colour of a ball in  
        one of three locations. This colour specifies the location of the  
        criterion colour that has to be matched by the agent's choice.  
         
        In this example, we assume that the agent has learned the generative  
        model of the game but does not know the likelihood mapping between latent  
        states and feedback or reward that tells us whether it's choice was  
        correct or incorrect. However, the agent is equipped with priors over the  
        likelihood mapping in question, encoding all possible (second-order)  
        rules of the kind described above. This enables it to evaluate the  
        likelihood of each prior model using Bayesian model reduction (starting  
        with prior based upon the Bayesian model average of prior models). These  
        marginal likelihoods can then be used to evaluate the expected  
        information gain over models, conditioned on each policy. The policies in  
        question here depend upon where the agent is looking and the choice it  
        commits to.  
         
        The expected information gain supplements the salience (information gain  
        about states) and novelty (information gain about parameters) terms in  
        expected free energy; thereby causing the agent to sample information  
        that best resolves uncertainty about which model is in the play. When  
        sufficiently confident (as scored by its beliefs about models) it can  
        then replace its posterior likelihood mapping with the model selected  
        from its model priors and, if correct, proceed as usual to secure as many  
        wins as possible.  
         
        In what follows, we first demonstrate the optimal behaviour of an agent  
        that knows the correct rule, and plans two steps into the future under  
        sophisticated inference. We then repeat the simulation removing prior  
        preferences (and deep planning) to let the expected information gain over  
        models predominate in action selection. When the log odds ratio of the  
        most likely model being the only viable model exceeds 16, preferences are  
        reinstated and the agent proceeds in an exploitative fashion. The ensuing  
        behaviour is characterised in terms of the agents confidence; i.e., the  
        expected precision or negentropy of beliefs over policies, performance  
        and rule discovery (as scored by the KL divergence between the true  
        likelihood mapping and the posterior encoded in Dirichlet counts  
        accumulated over successive trials.  
         
        see also: spm_MDP_BMR.m and spm_MPD_VB_XXX.m  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_reasoning.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_reasoning", *args, **kwargs)
