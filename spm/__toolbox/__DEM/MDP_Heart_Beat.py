from spm.__wrapper__ import Runtime


def MDP_Heart_Beat(*args, **kwargs):
    """
      This simulation uses a Markov Decision process formulation of active  
        inference to demonstrate the interaction between interoceptive and  
        exteroceptive perception. This relies upon the fact that the function of  
        exteroceptive sense organs depends upon oscillatory cycles in  
        interoceptive states. The example used here is the change in retinal  
        blood flow, and its influence on vision, during a cardiac cycle.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/MDP_Heart_Beat.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("MDP_Heart_Beat", *args, **kwargs)
