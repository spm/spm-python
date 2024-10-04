from spm.__wrap__ import _Runtime


def spm_dem_reach_x2J(*args, **kwargs):
  """  returns the joint posititions for a two-joint arm  
    FORMAT [J] = spm_dem_reach_x2J(x)  
     
    x    - hidden states (joint angles)  
    x    - hidden states  
      x(1) - joint angle  
      x(2) - joint angle  
     
    J1   - position of 1st joint  
    J2   - position of 2nd joint (relative to first)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_dem_reach_x2J.m)
  """

  return _Runtime.call("spm_dem_reach_x2J", *args, **kwargs)
