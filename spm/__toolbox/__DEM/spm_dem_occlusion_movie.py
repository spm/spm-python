from spm.__wrapper__ import Runtime


def spm_dem_occlusion_movie(*args, **kwargs):
    """
      creates a movie of visual pursuit with occlusion  
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_dem_occlusion_movie.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dem_occlusion_movie", *args, **kwargs, nargout=0)
