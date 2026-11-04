from spm._runtime import Runtime


def DEM_demo_DEM(*args, **kwargs):
    r"""
      Triple estimation of states, parameters and hyperparameters: This demo  
        focuses on estimating both the states and parameters to furnish a  
        complete system identification, given only the form of the system and its  
        responses to unknown input (c.f., DEM_demo_EM, which uses known inputs)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_demo_DEM.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_demo_DEM", *args, **kwargs, nargout=0)
