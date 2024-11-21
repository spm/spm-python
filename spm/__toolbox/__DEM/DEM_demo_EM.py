from spm.__wrapper__ import Runtime


def DEM_demo_EM(*args, **kwargs):
    """
      Dual estimation of parameters and hyperparameters; under known causes:  
        This demo focuses on conditional parameter estimation with DEM and  
        provides a comparative evaluation using EM.  This proceeds by removing  
        uncertainly about the input so that the D-step can be discounted.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_EM.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_EM", *args, **kwargs, nargout=0)
