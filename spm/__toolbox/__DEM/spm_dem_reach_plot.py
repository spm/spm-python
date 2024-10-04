from spm.__wrap__ import _Runtime


def spm_dem_reach_plot(*args, **kwargs):
  """  plots the trajectory of a two-joint arm  
    FORMAT [f]= spm_dem_reach_plot(DEM)  
     
    DEM - DEM structure from reaching simulations  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_dem_reach_plot.m)
  """

  return _Runtime.call("spm_dem_reach_plot", *args, **kwargs)
