from spm.__wrap__ import _Runtime


def spm_dem_occlusion_movie(*args, **kwargs):
  """  creates a movie of visual pursuit with occlusion  
    FORMAT spm_dem_occlusion_movie(DEM)  
     
    DEM - DEM structure from simulations  
     
    hidden causes and states  
   ==========================================================================  
    x    - hidden states:  
      x.o(1) - oculomotor angle  
      x.o(2) - oculomotor velocity  
      x.x(1) - target location - extrinsic coordinates  
     
    v    - causal states: force on target  
     
    g    - sensations:  
      g(1) - oculomotor angle (proprioception)  
      g(2) - oculomotor velocity  
      g(:) - visual input - intrinsic coordinates  
   --------------------------------------------------------------------------  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_dem_occlusion_movie.m)
  """

  return _Runtime.call("spm_dem_occlusion_movie", *args, **kwargs, nargout=0)
