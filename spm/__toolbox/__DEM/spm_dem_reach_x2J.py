from spm.__wrapper__ import Runtime


def spm_dem_reach_x2J(*args, **kwargs):
    """
      returns the joint posititions for a two-joint arm  
        FORMAT [J] = spm_dem_reach_x2J(x)  
         
        x    - hidden states (joint angles)  
        x    - hidden states  
          x(1) - joint angle  
          x(2) - joint angle  
         
        J1   - position of 1st joint  
        J2   - position of 2nd joint (relative to first)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_dem_reach_x2J.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dem_reach_x2J", *args, **kwargs)
