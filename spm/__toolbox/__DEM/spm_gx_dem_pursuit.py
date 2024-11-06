from spm.__wrapper__ import Runtime


def spm_gx_dem_pursuit(*args, **kwargs):
    """
      returns the prediction for visual pursuit  
        FORMAT [g] = spm_gx_dem_pursuit(x,v,P)  
         
        x    - hidden states:  
          o(1) - oculomotor angle  
          o(2) - oculomotor angle  
          x(1) - target location (visual) - extrinsic coordinates (Cartesian)  
          x(2) - target location (visual) - extrinsic coordinates (Cartesian)  
          a(:) - attractor (SHC) states  
         
        v    - hidden causes  
        P    - parameters  
         
        g    - sensations:  
          g(1) - oculomotor angle (proprioception)  
          g(2) - oculomotor angle (proprioception)  
          g(3) - target location (visual) - intrinsic coordinates (polar)  
          g(4) - target location (visual) - intrinsic coordinates (polar)  
          
        As for spm_dem_reach but with no visual target  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_gx_dem_pursuit.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_gx_dem_pursuit", *args, **kwargs)
