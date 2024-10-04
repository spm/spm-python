from spm.__wrap__ import _Runtime


def spm_fx_dem_reach(*args, **kwargs):
  """  returns the flow for a two-joint arm  
    FORMAT [f]= spm_fx_dem_reach(x,v,P)  
     
    x    - hidden states  
      x(1) - joint angle  
      x(2) - joint angle  
      x(3) - angular velocity  
      x(4) - angular velocity  
    v    - causal states  
      v(1) - target location (x)  
      v(2) - target location (y)  
      v(3) - cue strength  
    P    - parameters  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_fx_dem_reach.m)
  """

  return _Runtime.call("spm_fx_dem_reach", *args, **kwargs)
