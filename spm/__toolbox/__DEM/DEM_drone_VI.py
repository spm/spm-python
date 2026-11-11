from spm._runtime import Runtime


def DEM_drone_VI(*args, **kwargs):
    r"""
      Demo of domain factors in renormalising models  
       __________________________________________________________________________  
         
        This demonstration routine builds upon DEM_drone_VI by finessing the  
        generative model and, crucially, using fast structure learning to a  
        symbol a scale free (renormalising) generative model: i.e., an RGM. In  
        brief, this furnishes a generative model of a known scene that includes  
        events. For example, people moving around the scene. In more detail, an  
        RGM has learned automatically from latent states generated from a process  
        model with no drone movement. The ensuing RGM then generates sequences of  
        state transitions at the lowest level. To complete the RGM, the  
        generative model encoding the lowest level likelihood mapping between  
        latent states and (drone position and pose-dependent) outcomes replaces  
        the first level of the RGM, with suitable adjustments to match the  
        outputs of the second level RGM to the children in the first level (in a  
        way that the paths of latent states of the first level are generated).  
         
        Effectively, this equips the generative model with empirical priors that  
        inherit from loan dynamics in the environment; enabling the agent to  
        track moving things to resolve uncertainty about where things (e.g.,  
        people) will appear next. Note that this demonstration effectively places  
        knowledge about the scene at hand in the parameters of the likelihood  
        mapping from the second to the first level. In other words, this  
        demonstration is concerned with navigating in a known environment, where  
        knowledge is installed both about things that do not move and dynamics.  
        From the perspective of the latent states encoding the state of each  
        location, this means that some locations never change, while an empty  
        location can change to be occupied by the class of things that can move,  
        and vice versa. The temporal or serial dependencies on these transitions  
        encode movement and object permanence as one ascends the hierarchical  
        generative model that features Scale transformations in both space and  
        time.  
         
        In this example, the empirical priors afforded by the deeper levels of  
        the RGM applied to and only two the latent states associated to each  
        location. This leaves the state of the drone (that would be informed by  
        telemetry) as controllable states to illustrate planning as inference at  
        the lowest level (using explicit action in the usual way). This means  
        that the planning is only constrained or informed by posterior  
        predictions about the next state of the world.  
       __________________________________________________________________________  
        Copyright (C) 2019 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_drone_VI.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_drone_VI", *args, **kwargs)
