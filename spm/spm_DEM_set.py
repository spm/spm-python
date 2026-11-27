from spm._runtime import Runtime


def spm_DEM_set(*args, **kwargs):
    r"""
      Perform checks on DEM structures  
        FORMAT [DEM] = spm_DEM_set(DEM)  
         
        DEM.M  - hierarchical model  
        DEM.Y  - response variable, output or data  
        DEM.U  - explanatory variables, inputs or prior expectation of causes  
        DEM.X  - confounds  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_DEM_set.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_DEM_set", *args, **kwargs)
