from spm.__wrapper__ import Runtime


def spm_MDP_mountain_car(*args, **kwargs):
    """
      Demo for Discrete Markov Decision process (planning)  
        FORMAT spm_MDP_mountain_car(X,V,T))  
        X    - initial and goal position  
        V    - initial and goal velocity  
        T    - number of time-steps  
         
        This routine uses a Markov decisions process formulation of the mountain  
        car problem to illustrate prospective free energy minimization under a  
        variational Bayesian learning scheme. The key notion here is that the  
        agent represents future states and action (in a pullback sense), where it  
        has strong prior beliefs about future states. The intervening states and  
        actions are optimized with respect to current sensory data to provide  
        predictions about the next sensory state, which action fulfils. The  
        result is a planned trajectory through state space that realizes prior  
        beliefs in a prospective sense.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_MDP_mountain_car.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_MDP_mountain_car", *args, **kwargs, nargout=0)
