from spm._runtime import Runtime


def spm_dem_reach_movie(*args, **kwargs):
    r"""
      creates a movie of the trajectory of a two-joint arm  
        FORMAT spm_dem_reach_movie(DEM)  
         
        DEM - DEM structure from reaching simulations  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_dem_reach_movie.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dem_reach_movie", *args, **kwargs, nargout=0)
