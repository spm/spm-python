from spm.__wrap__ import _Runtime


def spm_fx_dem_pursuit(*args, **kwargs):
  """  returns the flow for visual pursuit demo  
    FORMAT [f]= spm_fx_dem_pursuit(x,v,P)  
     
    x    - hidden states:  
      x.o(1) - oculomotor angle  
      x.o(2) - oculomotor angle  
      x.x(1) - target location (visual) - extrinsic coordinates (Cartesian)  
      x.x(2) - target location (visual) - extrinsic coordinates (Cartesian)  
      x.a(:) - attractor (SHC) states  
     
    v    - hidden causes  
    P    - parameters  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_fx_dem_pursuit.m)
  """

  return _Runtime.call("spm_fx_dem_pursuit", *args, **kwargs)
