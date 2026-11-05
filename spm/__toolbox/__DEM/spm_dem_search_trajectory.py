from spm._runtime import Runtime


def spm_dem_search_trajectory(*args, **kwargs):
    r"""
      plots visual search in extrinsic and intrinsic coordinates  
        FORMAT spm_dem_search_trajectory(DEM)  
         
        DEM - {DEM} structures from visual search simulations  
         
        hidden causes and states  
       ==========================================================================  
        x    - hidden states:  
          o(1) - oculomotor angle  
          o(2) - oculomotor angle  
          x(1) - relative amplitude of visual hypothesis 1  
          x(2) - relative amplitude of visual hypothesis 2  
          x(3) - ...  
         
        v    - hidden causes  
         
        g    - sensations:  
          g(1) - oculomotor angle (proprioception - x)  
          g(2) - oculomotor angle (proprioception - y)  
          g(3) - retinal input - channel 1  
          g(4) - retinal input - channel 2  
          g(5) - ...  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_dem_search_trajectory.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dem_search_trajectory", *args, **kwargs, nargout=0)
