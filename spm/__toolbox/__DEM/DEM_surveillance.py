from spm.__wrapper__ import Runtime


def DEM_surveillance(*args, **kwargs):
    """
      Demo of active (visual) scene-construction  
       __________________________________________________________________________  
         
        This routine uses a Markov decision process formulation of active  
        inference (with belief propagation) to model active scene construction.  
        It focuses on a discrete state space representation of a dynamic scene;  
        generating visual snapshots at about the same frequency of saccadic eye  
        movements. The generative model starts with latent states that correspond  
        to natural kinds (e.g., objects) subject to natural laws (e.g., object  
        invariance, classical mechanics, occlusion, and so on). A second latent  
        factor (e.g., a 'where' stream) generates the fixation points in visual  
        space for saccadic eye movements. The factors corresponding to multiple  
        objects are themselves a Kronecker tensor product of attributes that  
        depend upon each other; for example, position, velocity, pose, and  
        non-spatial attributes that depend on spatial attributes. This  
        interdependence means that object-specific attributes cannot be  
        factorised; hence their combination as a tensor product (e.g., a 'what'  
        stream).  
         
        In what follows, we build a generative model, starting from state  
        transitions that entail natural laws. Position refers to radial  
        coordinates in egocentric space, implying a distinction between angular  
        and radial (depth) states - and likewise for motion. This allows us to  
        incorporate head orientation; in the form of head movements that  
        reorientate the direction of gaze - that also depends upon the deployment  
        of saccades in a head-centred frame of reference. Head movements are  
        implemented, in the generative model, as moving objects in the egocentric  
        frame of reference. This means that head movement is implemented via  
        action-dependent transitions in location, while saccades are implemented  
        via transitions among the latent states representing where gaze is  
        deployed (in a head-centred frame of reference).  
         
        Equipped with all of these hidden states, one can then complete a  
        relatively simple generative model by specifying the likelihood mapping  
        from hidden states to observations. This likelihood mapping is a high  
        dimensional tensor - encoding all the high order dependencies generating  
        visual input for the epoch in question. High order here refers to  
        dependencies such as the interaction between two objects in the same line  
        of sight that depends upon their relative depth to model occlusions.  
         
        These outcomes are themselves discrete and multimodal. a high acuity  
        modality models the parvocellular stream, with a restricted (central)  
        field of view. This is complemented by two other modalities with a more  
        peripheral field of view reporting contrast and motion energy, that is  
        not spatially resolved (cf, the magnocellular stream). Note that in this  
        construction (designed to generate the outputs of a computer vision  
        scheme) motion is converted into a categorical (present versus absent)  
        variable over discrete epochs of time. Note that the kind of scene  
        construction and representation is implemented in egocentric and head  
        centric frames of reference throughout. There is no part of the  
        generative model that requires an allocentric representation - and yet,  
        the agent can skilfully navigate a relatively complicated moving  
        environment. in the example here, there are two inanimate objects (that  
        play the role of landmarks) and an inanimate object (namely, a person who  
        occasionally engages the agent with eye contact). This setup allows the  
        simulation of reciprocal gaze and a primitive form of dyadic interaction.  
        In other words, the prior preferences of this agent are to position  
        itself and its direction of gaze to find someone who is looking at her.  
         
        The code below is briefly annotated to illustrate how to build a  
        generative model and then simulate active inference under that model, to  
        produce relatively realistic sampling of a visual scene; namely, active  
        scene construction. This inversion uses a sophisticated active inference  
        scheme based upon a recursive estimation of expected free energy. This  
        finesses the numerics because it uses belief propagation into the future  
        - as opposed to marginal (variational) message passing. The numerical  
        complexity of these models is a nontrivial issue: this is because most of  
        the heavy lifting in the generative model is in the connectivity encoding  
        dependencies that corresponds to high-dimensional tensors. In these  
        simulations, the connectivity tensors are represented in working memory;  
        whereas, in the brain or analogue (neuromorphic) implementations they  
        would be simpler to instantiate.  
       _________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_surveillance.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_surveillance", *args, **kwargs)
