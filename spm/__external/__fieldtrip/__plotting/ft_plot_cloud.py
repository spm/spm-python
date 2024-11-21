from spm.__wrapper__ import Runtime


def ft_plot_cloud(*args, **kwargs):
    """
      FT_PLOT_CLOUD visualizes spatially sparse scalar data as spheres or  
        spherical clouds of points and optionally 2D slices through those clouds  
         
        Use as  
          ft_plot_cloud(pos, val, ...)  
        where the first argument are the positions and the second argument are the values  
        for each location.  
         
        Optional input arguments should come in key-value pairs and can include  
          'cloudtype'          = 'cloud' (default) plots a group of spherically arranged points at each sensor position  
                                 'surf' plots a single spherical surface mesh at each sensor position  
          'scalerad'           = scale radius with val, can be 'yes' or 'no' (default = 'yes')  
          'radius'             = scalar, maximum radius of cloud (default = 4 mm)  
          'clim'               = 1x2 vector specifying the min and max for the colorscale  
          'unit'               = string, convert the sensor array to the specified geometrical units (default = [])  
          'mesh'               = string or Nx1 cell-array, triangulated mesh(es), see FT_PREPARE_MESH  
          'slice'              = requires 'mesh' as input (default = 'none')  
                                 '2d', plots 2D slices through the cloud with an outline of the mesh  
                                 '3d', draws an outline around the mesh at a particular slice  
         
        The following inputs apply when 'cloudtype' = 'cloud'  
          'rmin'               = scalar >= 1, minimum radius of cloud if scalerad = 'yes' (default = 1 mm)  
          'colormap'           = colormap for functional data, see COLORMAP  
          'colorgrad'          = 'white' or a scalar (e.g. 1), degree to which the saturatoin of points in cloud changes from its center  
          'ptsize'             = scalar, size of points in cloud (default = 1 mm)  
          'ptdensity'          = scalar, density of points in cloud (default = 20 per mm^3)  
          'ptgradient'         = scalar, degree to which density of points in cloud changes from its center (default = 0.5, i.e. uniform density)  
         
        The following inputs apply when 'slice' = '2d' or '3d'  
          'ori'                = 'x', 'y', or 'z', specifies the orthogonal plane which will be plotted (default = 'y')  
          'slicepos'           = 'auto' or Nx1 vector specifying the position of the  
                                 slice plane along the orientation axis (default = 'auto': chooses slice(s) with  
                                 the most data)  
          'nslices'            = scalar, number of slices to plot if 'slicepos' = 'auto (default = 1)  
          'minspace'           = scalar, minimum spacing between slices if nslices>1  
                                 (default = 1)  
          'intersectcolor'     = string, Nx1 cell-array, or Nx3 vector specifying line color (default = 'k')  
          'intersectlinestyle' = string or Nx1 cell-array, line style specification (default = '-')  
          'intersectlinewidth' = scalar or Nx1 vector, line width specification (default = 2)  
         
        The following inputs apply when 'cloudtype' = 'surf' and 'slice' = '2d'  
          'ncirc'           = scalar, number of concentric circles to plot for each  
                              cloud slice (default = 15) make this hidden or scale  
          'scalealpha'      = 'yes' or 'no', scale the maximum alpha value of the center circle  
                              with distance from center of cloud  
         
        See also FT_ELECTRODEPLACEMENT, FT_PLOT_SENS, FT_PLOT_TOPO, FT_PLOT_TOPO3D  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/ft_plot_cloud.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_plot_cloud", *args, **kwargs, nargout=0)
