from spm._runtime import Runtime


def DEM_federation(*args, **kwargs):
    r"""
      Demo of active (visual) scene-construction  
       __________________________________________________________________________  
         
        This demonstration illustrates the emergence of belief sharing and  
        distributed (i.e., federated) inference when posterior beliefs are  
        broadcast among multiple agents. It can be read from a number of  
        perspectives: from a systemic perspective, this emergence can be read as  
        the minimisation of joint free energy that ensues when inference,  
        learning and selection are simulated as a free energy minimising  
        processes. A more anthropomorphic interpretation is in terms of language  
        and communication; namely, the acquisition of language, and its  
        transmission over generations, in the spirit of cultural niche  
        construction.  
          
        The particular example here uses three agents that can be thought of as  
        three sentinels maintaining surveillance for potential predators.  
        Crucially, each of the three agents has a restricted field of view, such  
        that each can only see about 1/3 of the horizon. In addition to visual  
        and proprioceptive (gaze-related) observation modalities, each agent can  
        also hear the others (but not itself). The agents have a simple  
        (identity) likelihood mapping between posterior beliefs — about latent  
        states that are shared (or conserved) over agents — and output modalities  
        or communication channels.  
          
        Here, the birds report the location of a potential predator in terms of  
        its radial location in an allocentric frame of reference and its  
        proximity (near or far). In addition, the agents can report whether the  
        predator (i.e., subject of surveillance) is friendly or not. This active  
        inference is deliberately made difficult (in addition to the limited  
        field of view afforded each agent): first, the agents cannot see motion.  
        This means movement of the subject has to be inferred from successive  
        observations of location. This inference is crucial because it  
        underwrites predictions of location at the next time step, which are  
        broadcast to other agents. In the absence of this prediction, there would  
        be less predictive value for the other agents. Second, the disambiguation  
        between friend and foe is only possible when the predator is sufficiently  
        close to each bird.  
          
        This scheme uses a generalised MDP, in which the paths are assumed to be  
        unchanging during each epoch (unless they are controllable). This means  
        for each episode of the simulation the predator is moving continuously in  
        one direction or another (or remains stationary).  
          
        In what follows, we first demonstrate the utility of belief sharing, in  
        resolving uncertainty about latent states, when their consequences can  
        only be seen by one agent at a time. We then illustrate the acquisition  
        of language (i.e., likelihood mappings) using active learning or  
        accumulation of Dirichlet counts, where a child of one parent learns from  
        its parents and conspecifics. Finally, we illustrate the emergence of  
        language (i.e., precise and shared likelihood mappings) in an ensemble of  
        agents with initially imprecise, random likelihood tensors, when they are  
        exposed to the same environment. This emergence rests upon structure  
        learning in which priors over the Dirichlet counts of likelihood tensors  
        are updated using Bayesian model reduction – and the updates are in the  
        direction of maximising expected free energy or the mutual information of  
        the likelihood mapping. In short, distributed inference emerges from  
        minimising (variational and expected) free energy at three levels of  
        joint inference, learning and selection.  
       _________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_federation.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_federation", *args, **kwargs)
