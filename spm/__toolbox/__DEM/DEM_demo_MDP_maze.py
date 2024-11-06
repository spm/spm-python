from spm.__wrapper__ import Runtime


def DEM_demo_MDP_maze(*args, **kwargs):
    """
      Demo of active inference for epistemic foraging  
       __________________________________________________________________________  
         
        This routine uses the Markov decision process formulation of active  
        inference (with variational Bayes) to model foraging for information in a  
        three arm maze.  This demo illustrates variational free energy  
        minimisation in the context of Markov decision processes, where the agent  
        is equipped with prior beliefs that it will minimise expected free energy  
        in the future. This free energy is the free energy of future sensory  
        states expected under the posterior predictive distribution. It can be  
        regarded as a generalisation of the variational formulation of KL control  
        in which information gain or epistemic value is formulated explicitly.  
         
        In this example, the agent starts at the centre of a three way maze  
        which is baited with a reward in one of the two upper arms. However, the  
        rewarded arm changes from trial to trial.  Crucially, the agent can  
        identify where the reward (US) is located by accessing a cue (CS) in the  
        lower arm. This tells the agent whether the reward is on the left or the  
        right upper arm.  This means the optimal policy would first involve  
        maximising information gain or epistemic value by moving to the lower arm  
        and then claiming the reward this signified. Here, there are eight hidden  
        states (four locations times right or left reward), four control states  
        (that take the agent to the four locations) and 16 outcomes (four  
        locations times two cues times two rewards).  The central location has an  
        ambiguous or uninformative cue outcome, while the upper arms are rewarded  
        probabilistically with an 80% schedule.  
         
        A single trial is simulated followed by an examination of dopaminergic  
        responses to conditioned and unconditioned stimuli (cues and rewards). A  
        hierarchical version is then implemented, in which the mapping between  
        locations in the generative model and the generative process is unknown  
        and has to be learned.  
         
        see also: spm_MPD_game  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_MDP_maze.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_MDP_maze", *args, **kwargs)
