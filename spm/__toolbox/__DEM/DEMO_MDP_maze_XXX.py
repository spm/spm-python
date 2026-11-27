from spm._runtime import Runtime


def DEMO_MDP_maze_XXX(*args, **kwargs):
    r"""
      Demo of inductive inference based on a learned likelihood mapping  
       __________________________________________________________________________  
         
        This demonstration of active inference focuses on navigation and  
        planning. The idea is to demonstrate how epistemic foraging and goal  
        (target) directed behaviour are integrated in the minimisation of  
        expected free energy. In this illustration, and 10 x 10 maze is learned  
        through novelty-driven evidence accumulation - to learn the likelihood  
        mapping between hidden states (locations in the maze) and outcomes  
        (whether the current location is aversive or not). This accumulated  
        experience is then used to plan a path from a start to an end (target  
        location) under a task set specified by prior preferences over locations.  
         
        This version uses a belief propagation scheme (with deep policy searches)  
        to illustrate intentional behaviour. This search is constrained using  
        inductive inference; namely, placing priors over the subsequent states  
        that preclude regimes of state space that cannot access the final state.  
        These priors rest upon a time reversed protocol under allowable (learned)  
        state transitions. In effect, priors over the final state contextualise  
        priors over outcomes by precluding states that lie ahead, on a path of  
        least action that minimises expected free energy.The code below can be  
        edited to demonstrate different kinds of behaviour, under different  
        preferences, policy depth and precisions.  
         
        see also: spm_MPD_VB_XXX.m  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEMO_MDP_maze_XXX.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEMO_MDP_maze_XXX", *args, **kwargs)
