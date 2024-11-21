from spm.__wrapper__ import Runtime


def spm_dem_mdp_movie(*args, **kwargs):
    """
      creates a movie of visual search in extrinsic and intrinsic coordinates  
        FORMAT spm_dem_mdp_movie(DEM)  
         
        DEM - {DEM} structures from visual search simulations  
         
        hidden causes and states  
       ==========================================================================  
        x    - hidden states:  
          x(1) - oculomotor angle  
          x(2) - oculomotor angle  
        v    - hidden causes  
          v(1) - location of object  
          v(2) - location of object  
          v(3) - relative amplitude of visual hypothesis 1...  
         
        g    - sensations:  
          g(1) - oculomotor angle (proprioception - x)  
          g(2) - oculomotor angle (proprioception - y)  
          g(3) - retinal input - channel 1  
          g(4) - retinal input - channel 2  
          g(5) - ...  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_dem_mdp_movie.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dem_mdp_movie", *args, **kwargs, nargout=0)
