from spm.__wrapper__ import Runtime


def ft_plot_topo(*args, **kwargs):
    """
      FT_PLOT_TOPO interpolates and plots the 2-D spatial topography of the  
        potential or field distribution over the head  
         
        Use as  
          ft_plot_topo(x, y, val, ...)  
         
        Optional arguments should come in key-value pairs and can include  
          'gridscale'     = scalar, number of points along both directions for interpolation (default = 67)  
          'datmask'       = vector of same dimensions as val  
          'mask'          = cell-array with line segments that forms the mask (see FT_PREPARE_LAYOUT)  
          'outline'       = cell-array with line segments that for the outline (see  FT_PREPARE_LAYOUT)  
          'isolines'      = vector with values for isocontour lines (default = [])  
          'interplim'     = string, 'sensors' or 'mask' (default = 'sensors')  
          'interpmethod'  = string, 'nearest', 'linear', 'natural', 'cubic' or 'v4' (default = 'v4')  
          'style'         = can be 'surf', 'iso', 'isofill', 'surfiso', 'imsat', 'imsatiso', 'colormix'  
          'clim'          = [min max], limits for color scaling  
          'shading'       = string, 'none', 'flat', 'interp' (default = 'flat')  
          'parent'        = handle which is set as the parent for all plots (default = [])  
          'tag'           = string, the tag assigned to the plotted elements (default = '')  
         
        It is possible to plot the object in a local pseudo-axis (c.f. subplot), which is specfied as follows  
          'box'           = draw a box around the local axes, can be 'yes' or 'no'  
          'hpos'          = horizontal position of the lower left corner of the local axes  
          'vpos'          = vertical position of the lower left corner of the local axes  
          'width'         = width of the local axes  
          'height'        = height of the local axes  
          'hlim'          = horizontal scaling limits within the local axes  
          'vlim'          = vertical scaling limits within the local axes  
         
        See also FT_PLOT_TOPO3D, FT_PLOT_LAYOUT, FT_TOPOPLOTER, FT_TOPOPLOTTFR  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/ft_plot_topo.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_plot_topo", *args, **kwargs)
