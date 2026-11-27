from spm._runtime import Runtime


def DEM_demo_Lagrangian(*args, **kwargs):
    r"""
      Demo to illustrate divergence and curl free flow specified by a   
        Lagrangian and antisymmetric matrices. This example uses a double well   
        potential and Newtonian dynamics.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_demo_Lagrangian.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_demo_Lagrangian", *args, **kwargs, nargout=0)
