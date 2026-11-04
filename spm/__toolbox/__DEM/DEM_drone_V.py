from spm._runtime import Runtime


def DEM_drone_V(*args, **kwargs):
    r"""
      Demo of domain factors in the setting of active vision  
       __________________________________________________________________________  
         
        This demonstration routine builds upon DEM_drone_telemetry.m to  
        illustrate the role of domain factors in selecting the parents of  
        likelihood mappings. In particular, it leverages the specification of  
        parents (and children) using functional forms as opposed to tensors of  
        precomputed cell arrays of parents (i.e., id.fg). This takes the pressure  
        off memory when dealing with large cell tensors. The demonstration in  
        this routine is limited to (initial) exploration to build posterior  
        beliefs about a static environment.  
         
        In addition to showcasing the finessing of memory load incurred by using  
        precomputed cell tensors, it also replaces likelihood tensors with  
        function handles. This means that the likelihood mapping can be specified  
        in a functional form. These functions are multipurpose functions that  
        replace the sum product operators involving the likelihood tensors. These  
        operators include computing the log likelihood by taking the dot product  
        between some outcomes to generate a joint likelihood over latent states.  
        Conversely, they involve taking the dot product given some latent states  
        to generate outcomes in each modality. The functions are written such  
        that the requisite output arguments depend upon whether they are called  
        with a numeric array (i.e., distribution over outcomes) or a series of  
        cell arrays (i.e., marginal distributions over the latent states).  
         
        This demonstration uses a more realistic environment and dispenses with  
        proximity modalities to provide a more efficient scanning of the  
        environment. This efficiency inherits from the specification of log  
        likelihoods as marginals, as opposed to joint distributions over latent  
        states, when updating posteriors (see spm_VBX). In special cases, the  
        joint distribution can be marginalised; for example, by considering a  
        single output at, and only at, the depth of the first occluder.  
         
       __________________________________________________________________________  
        Copyright (C) 2019 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_drone_V.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_drone_V", *args, **kwargs)
