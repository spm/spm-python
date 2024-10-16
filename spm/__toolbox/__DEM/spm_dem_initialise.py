from spm.__wrapper__ import Runtime


def spm_dem_initialise(*args, **kwargs):
  """  Initialises parameter estimates for DEM structures  
    FORMAT [DEM] = spm_dem_initialise(DEM)  
     
    DEM.M  - hierarchical model  
    DEM.Y  - inputs or data  
    DEM.U  - prior expectation of causes  
    DEM.X  - observation confounds  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_dem_initialise.m)
  """

  return Runtime.call("spm_dem_initialise", *args, **kwargs)
