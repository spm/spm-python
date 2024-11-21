from spm.__wrapper__ import Runtime


def DEM_demo_DEM(*args, **kwargs):
    """
      Triple estimation of states, parameters and hyperparameters:  
        This demo focuses estimating both the states and parameters to furnish a  
        complete system identification, given only the form of the system and its  
        responses to unknown input (c.f., DEM_demo_EM, which uses known inputs)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_DEM.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_DEM", *args, **kwargs, nargout=0)
