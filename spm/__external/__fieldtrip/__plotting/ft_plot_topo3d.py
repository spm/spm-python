from spm.__wrapper__ import Runtime


def ft_plot_topo3d(*args, **kwargs):
    """
      FT_PLOT_TOPO3D visualizes a 3D topographic representation of the electric potential  
        or magnetic field distribution at the sensor locations.  
         
        Use as  
          ft_plot_topo3d(pos, val, ...)  
        where the channel positions are given as a Nx3 matrix and the values are  
        given as Nx1 vector.  
         
        Optional input arguments should be specified in key-value pairs and can include  
          'contourstyle'  = string, 'none', 'black', 'color' (default = 'none')  
          'isolines'      = vector with values at which to draw isocontours, or 'auto' (default = 'auto')  
          'facealpha'     = scalar, between 0 and 1 (default = 1)  
          'refine'        = scalar, number of refinement steps for the triangulation, to get a smoother interpolation (default = 0)  
          'neighbourdist' = number, maximum distance between neighbouring sensors (default is automatic)  
          'unit'          = string, 'm', 'cm' or 'mm' (default = 'cm')  
          'coordsys'      = string, assume the data to be in the specified coordinate system (default = 'unknown')  
          'axes'          = boolean, whether to plot the axes of the 3D coordinate system (default = false)  
         
        See also FT_PLOT_TOPO, FT_PLOT_SENS, FT_PLOT_MESH, FT_PLOT_HEADSHAPE,  
        FT_TOPOPLOTER, FT_TOPOPLOTTFR  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/ft_plot_topo3d.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_plot_topo3d", *args, **kwargs, nargout=0)
