from spm.__wrapper__ import Runtime


def spm_dem_reach_movie(*args, **kwargs):
    """
      creates a movie of the trajectory of a two-joint arm  
        FORMAT spm_dem_reach_movie(DEM)  
         
        DEM - DEM structure from reaching simulations  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_dem_reach_movie.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dem_reach_movie", *args, **kwargs, nargout=0)
