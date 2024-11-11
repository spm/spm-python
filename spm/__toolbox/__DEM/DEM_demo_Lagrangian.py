from spm.__wrapper__ import Runtime


def DEM_demo_Lagrangian(*args, **kwargs):
    """
      Demo to illustrate divergence and curl free flow specified by a   
        Lagrangian and antisymmetric matrices. This example uses a double well   
        potential and Newtonian dynamics.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_Lagrangian.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_Lagrangian", *args, **kwargs, nargout=0)
