from spm._runtime import Runtime


def spm_dem_initialise(*args, **kwargs):
    r"""
      Initialises parameter estimates for DEM structures  
        FORMAT [DEM] = spm_dem_initialise(DEM)  
         
        DEM.M  - hierarchical model  
        DEM.Y  - inputs or data  
        DEM.U  - prior expectation of causes  
        DEM.X  - observation confounds  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_dem_initialise.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dem_initialise", *args, **kwargs)
