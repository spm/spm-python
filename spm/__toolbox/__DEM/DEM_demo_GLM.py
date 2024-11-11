from spm.__wrapper__ import Runtime


def DEM_demo_GLM(*args, **kwargs):
    """
      Demo comparing DEM and ReML (restricted maximum likelihood) under a simple  
        general linear model (GLM).  Slight differences in the hyperpriors of both  
        schemes make this an interesting exercise.  Note that ReML uses a  
        covariance hyper-parameterisation; whereas DEM uses precision  
        hyperparameters.  This demo uses a non-hierarchical GLM and switches the  
        roles of parameters and causes to illustrate their equivalence under a   
        DEM inversion.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_GLM.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_GLM", *args, **kwargs, nargout=0)
