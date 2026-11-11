from spm._runtime import Runtime


def DEM_demo_filtering(*args, **kwargs):
    r"""
      State-space demo routine comparing Bayesian filtering and DEM:  The  
        system here is chosen to highlight changes in conditional moments  
        (including precision) induced by nonlinearities in the model.  A  
        comparative evaluation is provided using extended Kalman filtering and  
        particle filtering. Crucially, DEM and particle filtering deal gracefully  
        with nonlinearities, in relation to Kalman filtering.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_demo_filtering.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_demo_filtering", *args, **kwargs, nargout=0)
