from spm.__wrapper__ import Runtime


def spm_dem_cue_movie(*args, **kwargs):
    """
      creates a movie of cued pointing  
        FORMAT spm_dem_cue_movie(DEM,q)  
         
        DEM - DEM structure from reaching simulations  
        q   - flag switching from true to perceived reaching  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_dem_cue_movie.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dem_cue_movie", *args, **kwargs, nargout=0)
