from spm.__wrapper__ import Runtime


def DEM_FEP_Least_Action(*args, **kwargs):
    """
     --------------------------------------------------------------------------  
        This routine uses a Lorenz system to show that the most likely autonomous  
        path (or deterministic path) is uniquely identified by its initial and  
        final states. In other words, if we knew the end state of an autonomous  
        trajectory, then we would implicitly know the path taken from the initial  
        particular state, even if we did not know the external states. This point  
        is demonstrated using numerical analyses of the Lorenz system; treating  
        the first state and an active state and the third as an external state.  
        In this example, 1024 solutions are obtained from the same initial  
        particular (i.e., sensory and active) states but sampling from a Gaussian  
        distribution over external states. The ensuing trajectories over 128 time  
        bins of 1/128 seconds are shown in the left panels. The sample  
        distribution over active states is shown as a (scaled) histogram along  
        the x-axis. Paths that end within 1/8 of an arbitrary active state (here,  
        ?? = -4) are shown in red. The corresponding autonomous (i.e., active)  
        paths are shown as a function of time in the right panels. one can repeat  
        this analysis for different levels of random fluctuations; e.g.,log  
        precisions of 2 and 16. The key thing to observe is that as the amplitude  
        of random fluctuations decreases (i.e., its precision increases) the  
        paths that begin and end in the same place collapse to a single  
        trajectory of least action. This is the most likely or deterministic  
        path. Clearly, this behaviour rests upon a diffeomorphic mapping between  
        the initial and final states: for example, a final active state of -8 has  
        the least two paths of least action (xT in the code below).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_FEP_Least_Action.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_FEP_Least_Action", *args, **kwargs, nargout=0)
