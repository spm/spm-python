from spm._runtime import Runtime


def spm_dem_pursuit_movie(*args, **kwargs):
    r"""
      creates a movie of visual prusuit in extrinsic and intrinsic coordinates  
        FORMAT spm_dem_pursuit_movie(DEM)  
         
        DEM - DEM structure from reaching simulations  
         
        hidden causes and states  
       --------------------------------------------------------------------------  
        x    - hidden states:  
          x.o(1) - oculomotor angle  
          x.o(2) - oculomotor angle  
          x.x(1) - target location (visual) - extrinsic coordinates (Cartesian)  
          x.x(2) - target location (visual) - extrinsic coordinates (Cartesian)  
          x.a(:) - attractor (SHC) states  
         
        v    - causal states  
          v(1) - not used  
         
        g    - sensations:  
          g(1) - oculomotor angle (proprioception)  
          g(2) - oculomotor angle (proprioception)  
          g(3) - target location (visual) - intrinsic coordinates (polar)  
          g(4) - target location (visual) - intrinsic coordinates (polar)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_dem_pursuit_movie.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dem_pursuit_movie", *args, **kwargs, nargout=0)
