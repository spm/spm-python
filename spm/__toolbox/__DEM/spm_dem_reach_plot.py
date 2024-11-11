from spm.__wrapper__ import Runtime


def spm_dem_reach_plot(*args, **kwargs):
    """
      plots the trajectory of a two-joint arm  
        FORMAT [f]= spm_dem_reach_plot(DEM)  
         
        DEM - DEM structure from reaching simulations  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_dem_reach_plot.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dem_reach_plot", *args, **kwargs)
