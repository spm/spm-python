from spm.__wrapper__ import Runtime


def DEMO_niche_construction(*args, **kwargs):
    """
      Demo of niche construction using active inference  
       __________________________________________________________________________  
         
        The free-energy principle is an attempt to explain the structure of the  
        agent and its brain, starting from the fact that an agent exists (Friston  
        and Stephan, 2007; Friston et al., 2010). More specifically, it can be  
        regarded as a systematic attempt to understand the 'fit' between an  
        embodied agent and its niche, where the quantity of free-energy is a  
        measure for the 'misfit' or disattunement (Bruineberg and Rietveld, 2014)  
        between agent and environment. This paper offers a proof-of-principle  
        simulation of niche construction under the free-energy principle. The key  
        point of this paper is that the minimum of free-energy is not at a point  
        in which the agent is maximally adapted to the statistics of a static  
        environment, but can better be conceptualized an attracting manifold  
        within the joint  agent-environment state-space as a whole, which the  
        system tends toward through mutual interaction. We will provide a general  
        introduction to active inference and the free-energy principle. Using  
        Markov Decision Processes (MDPs), we then describe a canonical generative  
        model and the ensuing update equations that minimize free-energy. We then  
        apply these equations to simulations of foraging in an environment; in  
        which an agent learns the most efficient path to a pre-specified  
        location. In some of those simulations, unbeknownst to the agent, the  
        environment changes as a function of the activity of the agent (i.e.  
        unintentional niche construction occurs). We will show how, depending on  
        the relative inertia of the environment and agent, the joint  
        agent-environment system moves to different attracting sets of jointly  
        minimized free-energy.  
         
        see also: spm_MPD_VB_X.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEMO_niche_construction.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEMO_niche_construction", *args, **kwargs, nargout=0)
