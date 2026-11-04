from spm._runtime import Runtime


def DEM_drone_vision(*args, **kwargs):
    r"""
      Demo of domain factors in the setting of active vision  
       __________________________________________________________________________  
         
        This routine illustrates weight sharing in the context of partially  
        observed Markov decision processes. Specifically, it considers the  
        problem of building posterior beliefs (c.f., a cognitive map) based upon  
        spas sampling of an (unchanging) environment using the same likelihood  
        mappings for each modality that conditioning the subset of hidden factors  
        (i.e., the states of some location) that constitute the domain (i.e.,  
        parents)  of the likelihood mapping. In other words, contextualising the  
        allocentric representation of the environment to generate egocentric  
        observations. Effectively, this means that one can encode the requisite  
        projective geometry, not in the likelihood mappings, but in the hidden  
        states to which they refer.  
         
        The particular problem here models the environment as a collection of  
        conditionally independent factors, where each factor corresponds to a  
        location (a point on a 3D grid representation of the world). The levels  
        of each factor encode the state or (semantic) class of each location. The  
        conditional independence of the latent factors means that a subset of  
        factors are the parents of the likelihood mapping at any one time. And  
        these parents depend upon where a drone is currently looking.  
          
        A drone can fly around the environment with several lines of sight  
        (corresponding to the number of modalities). Depending upon the location  
        and orientation of the drone, a small number of locations are specified  
        to generate what would be seen from that perspective. This means there  
        are hidden factors pertaining to the location and orientation of the  
        drone and a set of hidden factors corresponding to the state of the  
        environment each location. The former are controllable, the latter are  
        not. In this setup, the configuration of the environment is encoded by  
        beliefs and exploration or navigation rests upon the expected information  
        gain about states (as opposed to parameters). One can also include an  
        expected cost of flying too close to locations with certain attributes.  
         
        Note that this requires two sets of variational updates — to update  
        posteriors over the state of the drone (based upon the likelihood of  
        observations from different perspectives), and to update posteriors over  
        the state of the environment (based upon the likelihood of observations,  
        given that perspective). In principle, this allows the drone to infer  
        both the environment and its relationship to that environment; although,  
        in practice, we will illustrate the behaviour of a drone given precise  
        beliefs about its initial state, or precise beliefs about the world  
       __________________________________________________________________________  
        Copyright (C) 2019 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_drone_vision.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_drone_vision", *args, **kwargs)
