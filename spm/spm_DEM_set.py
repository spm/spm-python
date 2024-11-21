from spm.__wrapper__ import Runtime


def spm_DEM_set(*args, **kwargs):
    """
      Perform checks on DEM structures  
        FORMAT [DEM] = spm_DEM_set(DEM)  
         
        DEM.M  - hierarchical model  
        DEM.Y  - response variable, output or data  
        DEM.U  - explanatory variables, inputs or prior expectation of causes  
        DEM.X  - confounds  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_DEM_set.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_DEM_set", *args, **kwargs)
