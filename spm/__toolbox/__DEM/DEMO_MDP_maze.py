from spm.__wrapper__ import Runtime


def DEMO_MDP_maze(*args, **kwargs):
    """
      Demo of mixed continuous and discrete state space modelling  
       __________________________________________________________________________  
         
        This demonstration of active inference focuses on navigation and planning  
        in a fairly complicated maze. The idea is to demonstrate how epistemic  
        foraging and goal (target) directed behaviour are integrated in the  
        minimisation of expected free energy. In this illustration, and 8 x 8  
        maze is learned through novelty driven evidence accumulation - to learn  
        the likelihood mapping between hidden states (locations in the maze) and  
        outcomes (whether the current location is open or closed). This  
        accumulated experience is then used to plan a path from a start to an end  
        (target location) under a task set specified by prior preferences over  
        locations. These priors are based upon a simple diffusion (CF backwards  
        induction) heuristic that specifies subgoals. The subgoals (i.e.,  
        locations) contain the most paths from the target within the horizon of  
        the current policy.  
         
        We will first illustrate the novelty driven epistemic foraging that  
        efficiently scans the maze to learn its structure. We then simulate  
        planning of (shortest path) trajectory to the target under the assumption  
        the maze has been previously learned. Finally, we consider exploration  
        under prior preferences to simulate behaviour when both epistemic and  
        goal directed imperatives are in play. The focus on this demo is on  
        behavioural and electrophysiological responses over moves.  
         
        A key aspect of this formulation is the  hierarchical decomposition of  
        goal directed behaviour into subgoals that are within the horizon of a  
        limited policy - here, to moves that correspond to a trial. The prior  
        preferences then contextualise each policy or trial to ensure that the  
        ultimate goal is achieved.  
         
        Empirically, this sort of construction suggests the existence of Path  
        cells; namely, cells who report the initial location of any subsequence  
        and continue firing until the end of the local path. This is illustrated  
        by plotting simulated activity as a function of trajectories during   
        exploration.  
         
        see also: spm_MPD_VB_X.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEMO_MDP_maze.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEMO_MDP_maze", *args, **kwargs)
