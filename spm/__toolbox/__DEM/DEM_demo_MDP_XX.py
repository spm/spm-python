from spm.__wrapper__ import Runtime


def DEM_demo_MDP_XX(*args, **kwargs):
    """
      Demo of active inference (T-maze): belief propagation scheme  
       __________________________________________________________________________  
         
        This routine uses a Markov decision process formulation of active  
        inference (with belief propagation) to model foraging for information in  
        a three arm maze.  This demo illustrates active inference in the context  
        of Markov decision processes, where the agent is equipped with prior  
        beliefs that it will minimise expected free energy in the future. This  
        free energy is the free energy of future sensory states expected under  
        the posterior predictive distribution. It can be regarded as a  
        generalisation of KL control that incorporates information gain or  
        epistemic value.  
         
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
         
        This version focuses on a sophisticated AI implementation that replaces  
        policies (i.e., ordered sequences of actions) with a deep tree search  
        over all combinations of actions. This deep search evaluates the expected  
        free energy under outcomes following an action and the ensuing hidden  
        state. The average over  hidden states and future actions is then  
        accumulated to provide the free energy expected under a particular course  
        of action in the immediate future. Notice that the free energy expected  
        under the next action is not the expected free energy following that  
        action. In other words, there is a subtle distinction between taking an  
        expectation under the posterior predictive distribution over outcomes and  
        the expectation of free energy over outcomes. This scheme is  
        sophisticated in the sense that the consequences of action for posterior  
        beliefs enter into the evaluation of expected free energy.  
         
        see also: DEM_demo_MDP_habits.m and spm_MPD_VB_X.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_MDP_XX.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_MDP_XX", *args, **kwargs)
