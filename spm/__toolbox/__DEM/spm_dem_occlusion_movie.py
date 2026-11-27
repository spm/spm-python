from spm._runtime import Runtime


def spm_dem_occlusion_movie(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_dem_occlusion_movie.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dem_occlusion_movie", *args, **kwargs, nargout=0)
