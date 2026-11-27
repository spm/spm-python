from spm._runtime import Runtime


def DEM_drone_telemetry(*args, **kwargs):
    r"""
      Demo of domain factors in the setting of active vision  
       __________________________________________________________________________  
         
        This routine illustrates a kind of SLAM (simultaneous localistion and  
        mapping) powered by active inference. The generative model is lightweight  
        in terms of memory; thereby eluding the von Neumann bottleneck. It  
        introduces a number of innovations. First, large tensors are replaced by  
        function handles that return requisite indices and probability  
        distributions on the fly (as a function of domain factors and states,  
        respectively). This precludes sum-product operators in the generative  
        process and takes the pressure off precomputed indices conditioned upon  
        domain factors. Note that outcomes are specified probabilistically;  
        enabling suitable uncertainty about sensor inputs (e.g., semantic  
        classification of locations that are out of range).  
         
        Second, action is now handled more realistically by selecting the action  
        that maximises the accuracy under posterior predictions. In other  
        words, action is explicitly determined based on the consequences in a  
        subspace of (telemetry) outcomes.  
          
        Third, this necessitates the provision of telemetry in terms of position,  
        pose and (lidar) depth along rays. Finally, the depth of each ray (i.e.,  
        line of sight) is treated as a latent state that is directly informed by  
        (lidar) measurements — and used as a domain factor to select the  
        appropriate likelihood mapping. This means that, in the generative model,  
        there is no need to model occlusion; this modelling is offloaded to the  
        generative process using the functional form of the requisite likelihood  
        mapping.  
          
        The above scheme allows for more rays of greater depth than previously  
        afforded by tensor parameterisation. However, the price paid is compute  
        time, which scales with the number of rays. Biomimetically, this can be  
        regarded as an exhaustive saccadic search over all rays. This follows  
        because the belief updating accumulates evidence from the likelihood of  
        each ray sequentially. For simplicity, the likelihood mappings are  
        assumed to be very precise; given the course graining afforded by  
        discrete state space models.  
       __________________________________________________________________________  
        Copyright (C) 2019 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_drone_telemetry.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_drone_telemetry", *args, **kwargs)
