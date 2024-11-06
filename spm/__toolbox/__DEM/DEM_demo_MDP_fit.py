from spm.__wrapper__ import Runtime


def DEM_demo_MDP_fit(*args, **kwargs):
    """
      Demo of active inference for trust games  
       __________________________________________________________________________  
         
        This routine uses a Markov decision process formulation of active  
        inference (with variational Bayes) to model foraging for information in a  
        three arm maze.  This demo illustrates the inversion of single-subject  
        and group data to make inferences about subject-specific parameters -  
        such as their prior beliefs about precision and utility. We first  
        generate some synthetic data for a single subject and illustrate the  
        recovery of key parameters using variational Laplace. We then consider  
        the inversion of multiple trials from a group of subjects to illustrate  
        the use of empirical Bayes in making inferences at the between-subject  
        level. Finally, we demonstrate the use of Bayesian cross-validation to  
        retrieve out-of-sample estimates (and classification of new subjects).  
         
        In this example, an agent starts at the centre of a three way maze that  
        is baited with a reward in one of the two upper arms. However, the  
        rewarded arm changes from trial to trial.  Crucially, the agent can  
        identify where the reward (US) is located by accessing a cue (CS) in the  
        lower arm. This tells the agent whether the reward is on the left or the  
        right upper arm. This means the optimal policy would first involve  
        maximising information gain or epistemic value by moving to the lower arm  
        and then claiming the reward thus signified. Here, there are eight hidden  
        states (four locations times right or left reward), four control states  
        (that take the agent to the four locations) and seven outcomes (three  
        locations times two cues plus the centre).  The central location has an  
        ambiguous or uninformative outcome, and the upper arms are rewarded  
        probabilistically.  
         
        see also: spm_MPD_VB.m, spm_dcm_mdp.m and spm_nlsi_Newton.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_MDP_fit.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_MDP_fit", *args, **kwargs)
