from spm.__wrapper__ import Runtime


def DEM_demo_MDP_X(*args, **kwargs):
    """
      Demo of active inference for trust games  
       __________________________________________________________________________  
         
        This routine uses a Markov decision process formulation of active  
        inference (with variational Bayes) to model foraging for information in a  
        three arm maze.  This demo illustrates variational free energy  
        minimisation in the context of Markov decision processes, where the agent  
        is equipped with prior beliefs that it will minimise expected free energy  
        in the future. This free energy is the free energy of future sensory  
        states expected under the posterior predictive distribution. It can be  
        regarded as a generalisation of the variational formulation of KL control  
        in which information gain or epistemic value is formulated explicitly.  
         
        In this example, the agent starts at the centre of a three way maze which  
        is baited with a reward in one of the two upper arms. However, the  
        rewarded arm changes from trial to trial.  Crucially, the agent can  
        identify where the reward (US) is located by accessing a cue (CS) in the  
        lower arm. This tells the agent whether the reward is on the left or the  
        right upper arm.  This means the optimal policy would first involve  
        maximising information gain or epistemic value by moving to the lower arm  
        and then claiming the reward this signified. Here, there are eight hidden  
        states (four locations times right or left reward), four control states  
        (that take the agent to the four locations) and four exteroceptive  
        outcomes (that depend on the agents locations) plus three interoceptive  
        outcomes indicating reward (or not).  
         
        This version focuses on factorising the hidden states causing  
        (factorised) outcomes. This factorisation is implicit in the tensor  
        production used in the companion demo.  Here the factorisation is  
        explicit enabling us to model multiple modalities (outcome factors) and  
        distinct hidden causes of observation (hidden state factors like what and  
        where). The behaviour is formally similar to the vanilla scheme but  
        allows a much more intuitive (and possibly flexible) model specification.  
         
        see also: DEM_demo_MDP_habits.m and spm_MPD_VB_X.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_MDP_X.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_MDP_X", *args, **kwargs)
