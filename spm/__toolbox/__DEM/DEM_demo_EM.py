from spm._runtime import Runtime


def DEM_demo_EM(*args, **kwargs):
    r"""
      Dual estimation of parameters and hyperparameters; under known causes:  
        This demo focuses on conditional parameter estimation with DEM and  
        provides a comparative evaluation using EM.  This proceeds by removing  
        uncertainly about the input so that the D-step can be discounted.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_demo_EM.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_demo_EM", *args, **kwargs, nargout=0)
