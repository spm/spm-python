from spm._runtime import Runtime


def MDP_DEM_Oculomotion_demo(*args, **kwargs):
    r"""
      Demo of mixed models for oculmotor behaviour  
         
       __________________________________________________________________________  
         
        This demo ilustrates the use of mixed (continuous and discrete)  
        generative models in simulating oculomotion. An MDP model is used to  
        select locations in visual space, and a continuous model is used to  
        implement these decisions. See also DEM_demo_MDP_DEM.m.  
        For a version of this routine with simulated pharmacological  
        interventions (and a delay-period task) please see:   
        MDP_DEM_Oculomotion_Pharma_demo.m  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/MDP_DEM_Oculomotion_demo.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("MDP_DEM_Oculomotion_demo", *args, **kwargs)
