from spm.__wrapper__ import Runtime


def spm_dem_initialise(*args, **kwargs):
    """
      Initialises parameter estimates for DEM structures  
        FORMAT [DEM] = spm_dem_initialise(DEM)  
         
        DEM.M  - hierarchical model  
        DEM.Y  - inputs or data  
        DEM.U  - prior expectation of causes  
        DEM.X  - observation confounds  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_dem_initialise.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dem_initialise", *args, **kwargs)
