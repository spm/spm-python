from spm._runtime import Runtime


def spm_gx_dem_reach(*args, **kwargs):
    r"""
      returns the prediction for a two-joint arm  
        FORMAT [g]= spm_gx_dem_reach(x,v,P)  
         
        x    - hidden states  
          x(1) - joint angle  
          x(2) - joint angle  
          x(3) - angular velocity  
          x(4) - angular velocity  
        v    - causal states  
          v(1) - target location (x)  
          v(2) - target location (y)  
          v(3) - force (cue strength)  
        P    - parameters  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_gx_dem_reach.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_gx_dem_reach", *args, **kwargs)
