from spm.__wrapper__ import Runtime


def ft_plot_dipole(*args, **kwargs):
    """
      FT_PLOT_DIPOLE makes a 3-D representation of a dipole using a sphere and a stick  
        pointing along the dipole orientation  
         
        Use as  
          ft_plot_dipole(pos, mom, ...)  
        where pos and mom are the dipole mosition and moment.  
         
        Optional input arguments should be specified in key-value pairs and can include  
          'diameter'  = number indicating sphere diameter (default = 'auto')  
          'length'    = number indicating length of the stick (default = 'auto')  
          'thickness' = number indicating thickness of the stick (default = 'auto')  
          'color'     = [r g b] values or string, for example 'brain', 'cortex', 'skin', 'black', 'red', 'r' (default = 'r')  
          'alpha'     = alpha value of the plotted dipole  
          'scale'     = scale the dipole with the amplitude, can be 'none',  'both', 'diameter', 'length' (default = 'none')  
          'unit'      = 'm', 'cm' or 'mm', used for automatic scaling (default = 'cm')  
          'coordsys'  = string, assume the data to be in the specified coordinate system (default = 'unknown')  
          'axes'      = boolean, whether to plot the axes of the 3D coordinate system (default = false)  
          'tag'       = string, the tag assigned to the plotted elements (default = '')   
         
        Example  
          ft_plot_dipole([0 0 0], [1 2 3], 'color', 'r', 'alpha', 1)  
         
        See also FT_PLOT_MESH, FT_PLOT_HEADMODEL, FT_PLOT_HEADSHAPE, FT_PLOT_ORTHO,  
        QUIVER3, PLOT3  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/ft_plot_dipole.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_plot_dipole", *args, **kwargs)
