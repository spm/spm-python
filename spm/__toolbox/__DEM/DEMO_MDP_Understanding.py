from spm._runtime import Runtime


def DEMO_MDP_Understanding(*args, **kwargs):
    r"""
      This demo uses a hierarchical version of the ubiquitous T-maze demo, in  
        which the agent is equipped with a space of hypotheses about why it chose  
        to act in a certain way. This means that, when queried, it is able to  
        communicate an explanation for its actions.  
         
        see also: DEM_demo_MDP_X.m and spm_MPD_VB_X.m  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEMO_MDP_Understanding.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEMO_MDP_Understanding", *args, **kwargs)
