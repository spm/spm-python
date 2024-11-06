from spm.__wrapper__ import Runtime


def DEM_demo_filtering(*args, **kwargs):
    """
      State-space demo routine comparing Bayesian filtering and DEM:  The  
        system here is chosen to highlight changes in conditional moments  
        (including precision) induced by nonlinearities in the model.  A  
        comparative evaluation is provided using extended Kalman filtering and  
        particle filtering. Crucially, DEM and particle filtering deal gracefully  
        with nonlinearities, in relation to Kalman filtering.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_filtering.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_filtering", *args, **kwargs, nargout=0)
