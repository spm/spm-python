from spm.__wrap__ import _Runtime


def spm_DEM_set(*args, **kwargs):
  """  Perform checks on DEM structures  
    FORMAT [DEM] = spm_DEM_set(DEM)  
     
    DEM.M  - hierarchical model  
    DEM.Y  - response variable, output or data  
    DEM.U  - explanatory variables, inputs or prior expectation of causes  
    DEM.X  - confounds  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_DEM_set.m)
  """

  return _Runtime.call("spm_DEM_set", *args, **kwargs)
