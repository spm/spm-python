from spm.__wrap__ import _Runtime


def spm_dem_reach_movie(*args, **kwargs):
  """  creates a movie of the trajectory of a two-joint arm  
    FORMAT spm_dem_reach_movie(DEM)  
     
    DEM - DEM structure from reaching simulations  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_dem_reach_movie.m)
  """

  return _Runtime.call("spm_dem_reach_movie", *args, **kwargs, nargout=0)
