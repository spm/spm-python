from spm._runtime import Runtime


def spm_RDP_radius(*args, **kwargs):
    r"""
      BMR of superordinate states based upon predicted outcomes  
        FORMAT [R,g,f,r] = spm_RDP_radius(MDP,h,c)  
        MDP  - cell array of MDP structures  
        h    - list of goal states  
        c    - list of cost states  
         
        R    - Ajaceny matrix among h  
        g    - goal states with children  
        f    - goal states on attractor  
        r    - radius  
         
        This routine returns the radius of each intended (goal) state for the  
        leading factor of a renormalising generative model. The radius is defined  
        as the maximum number of transitions between an orphan state (with no  
        parents) and the intended state.   
         
        In addition, it computes the adjacency among goal states in terms of  
        whether one goal state can be accessed from another. This allows one to  
        identify a subset of goal states that constitute an orbit (c.f., pullback  
        attractor).  
         
        see: https://en.wikipedia.org/wiki/Absorbing_Markov_chain  
       __________________________________________________________________________  
        Copyright (C) Karl Friston  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_RDP_radius.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_RDP_radius", *args, **kwargs)
