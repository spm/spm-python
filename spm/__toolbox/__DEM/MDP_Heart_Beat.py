from spm._runtime import Runtime


def MDP_Heart_Beat(*args, **kwargs):
    r"""
      This simulation uses a Markov Decision process formulation of active  
        inference to demonstrate the interaction between interoceptive and  
        exteroceptive perception. This relies upon the fact that the function of  
        exteroceptive sense organs depends upon oscillatory cycles in  
        interoceptive states. The example used here is the change in retinal  
        blood flow, and its influence on vision, during a cardiac cycle.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/MDP_Heart_Beat.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("MDP_Heart_Beat", *args, **kwargs)
