from spm._runtime import Runtime


def spm_gx_dem_write(*args, **kwargs):
    r"""
      returns the prediction for a two-joint arm (writing example)  
        FORMAT [g]= spm_gx_dem_write(x,v,P)  
         
        x    - hidden states:  
          x(1) - joint angle  
          x(2) - joint angle  
          x(3) - angular velocity  
          x(4) - angular velocity  
         
        v    - hidden causes  
        P    - parameters  
         
        g    - sensations:  
          g(1) - joint angle (proprioception)  
          g(2) - joint angle (proprioception)  
          g(3) - arm location (visual)  
          g(4) - arm location (visual)  
          
        As for spm_dem_reach but with no visual target  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_gx_dem_write.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_gx_dem_write", *args, **kwargs)
