from spm._runtime import Runtime


def DEM_drone_inspection(*args, **kwargs):
    r"""
      Demo of domain factors in the setting of active vision  
       __________________________________________________________________________  
         
        This demonstration routine illustrates active inference in the service of  
        inspecting objects in the scene; specifically, furniture or plant in a  
        room. The routine demonstrates three aspects of the ensuing behaviour.  
        First, the agent (e.g., cleaning robot) explores the room to form a  
        cognitive map of where things are. Objects (e.g., tables) that are  
        cleanable are recognised in terms of belonging to a cleanable class that  
        may be clean (dark green) or unclean (light green). Having established  
        precise posterior beliefs about the scene, the agent is equipped with  
        prior beliefs that each cleanable location (i.e., surface) can either be  
        clean or unclean and is given prior preferences for seeing (and  
        implicitly cleaning or spraying) unclean surfaces. The agent then  
        resolves uncertainty about whether surfaces are clean or unclean and  
        observes them to be clean when and only when, they have been observed  
        (and implicitly cleaned). This is because the state of the world (i.e.,  
        generative process) is always clean; however, the agent is not convinced  
        about this until it has seen clean surfaces for itself. Finally, the  
        agent goes home after completing its cleaning task using inductive  
        inference to specify its sleeping place (avoiding obstacles in the usual  
        way).  
         
        This example assumes local telemetry is available; in other words, the  
        position relative to some arbitrary (allocentric) frame of reference is  
        known — and the agent is equipped with both depth and RGB sensors, where  
        the RGB data are (semantically) segmented into eight classes using some  
        amortisation (computer vision) scheme. The agent has four degrees of  
        freedom. It can move on the floor in two dimensions. It%s sensors are  
        mounted on a vertical pole and can be moved up and down and rotated.  
         
       __________________________________________________________________________  
        Copyright (C) 2019 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_drone_inspection.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_drone_inspection", *args, **kwargs)
