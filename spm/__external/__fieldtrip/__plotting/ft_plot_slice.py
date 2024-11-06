from spm.__wrapper__ import Runtime


def ft_plot_slice(*args, **kwargs):
    """
      FT_PLOT_SLICE plots a single slice that cuts through a 3-D volume and interpolates  
        the data if needed.  
         
        Use as  
          ft_plot_slice(dat, ...)  
        or  
          ft_plot_slice(dat, mask, ...)  
        where dat and mask are equal-sized 3-D arrays.  
         
        Additional options should be specified in key-value pairs and can be  
          'transform'    = 4x4 homogeneous transformation matrix specifying the mapping from  
                           voxel coordinates to the coordinate system in which the data are plotted.  
          'location'     = 1x3 vector specifying a point on the plane which will be plotted  
                           the coordinates are expressed in the coordinate system in which the  
                           data will be plotted. location defines the origin of the plane  
          'orientation'  = 1x3 vector specifying the direction orthogonal through the plane  
                           which will be plotted (default = [0 0 1])  
          'unit'         = string, can be 'm', 'cm' or 'mm' (default is automatic)  
          'coordsys'     = string, assume the data to be in the specified coordinate system (default = 'unknown')  
          'resolution'   = number (default = 1 mm)  
          'datmask'      = 3D-matrix with the same size as the data matrix, serving as opacitymap  
                           If the second input argument to the function contains a matrix, this  
                           will be used as the mask  
          'maskstyle'    = string, 'opacity' or 'colormix', defines the rendering  
          'background'   = needed when maskstyle is 'colormix', 3D-matrix with  
                           the same size as the data matrix, serving as  
                           grayscale image that provides the background  
          'opacitylim'   = 1x2 vector specifying the limits for opacity masking  
          'interpmethod' = string specifying the method for the interpolation, see INTERPN (default = 'nearest')  
          'colormap'     = string, see COLORMAP  
          'clim'         = 1x2 vector specifying the min and max for the colorscale  
          'facealpha'    = transparency when no mask is specified, between 0 and 1 (default = 1)  
          'tag'          = string, the tag assigned to the plotted elements (default = '')  
         
        You can plot the slices from the volume together with an intersection of the slices  
        with a triangulated surface mesh (e.g. a cortical sheet) using  
          'intersectmesh'       = triangulated mesh, see FT_PREPARE_MESH  
          'intersectcolor'      = string, color specification  
          'intersectlinestyle'  = string, line specification  
          'intersectlinewidth'  = number  
         
        See also FT_PLOT_ORTHO, FT_PLOT_MONTAGE, FT_SOURCEPLOT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/ft_plot_slice.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_plot_slice", *args, **kwargs)
