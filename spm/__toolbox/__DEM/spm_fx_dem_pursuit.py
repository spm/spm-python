from spm._runtime import Runtime


def spm_fx_dem_pursuit(*args, **kwargs):
    """
      returns the flow for visual pursuit demo  
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_fx_dem_pursuit.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_fx_dem_pursuit", *args, **kwargs)
