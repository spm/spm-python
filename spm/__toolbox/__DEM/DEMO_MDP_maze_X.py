from spm.__wrapper__ import Runtime


def DEMO_MDP_maze_X(*args, **kwargs):
    """
      Demo of sophisticated inference and novelty (i.e.,planning to learn)  
       __________________________________________________________________________  
         
        This demonstration of active inference focuses on navigation and  
        planning. The idea is to demonstrate how epistemic foraging and goal  
        (target) directed behaviour are integrated in the minimisation of  
        expected free energy. In this illustration, and 8 x 8 maze is learned  
        through novelty driven evidence accumulation - to learn the likelihood  
        mapping between hidden states (locations in the maze) and outcomes  
        (whether the current location is aversive or not). This accumulated  
        experience is then used to plan a path from a start to an end (target  
        location) under a task set specified by prior preferences over locations.  
        These priors are based upon the distance between the current location and  
        a target location.  
         
        This version uses a belief propagation scheme (with deep policy searches)  
        to illustrate prospective behaviour; namely, selecting policies or  
        trajectories that transiently increased Bayesian risk. The code below can  
        be edited to demonstrate different kinds of behaviour, under different  
        preferences, policy depth and precisions.  
         
        see also: DEM_MDP_maze.m and spm_MPD_VB_X.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEMO_MDP_maze_X.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEMO_MDP_maze_X", *args, **kwargs)
