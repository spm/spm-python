from spm.__wrapper__ import Runtime


def ft_plot_box(*args, **kwargs):
    """
      FT_PLOT_BOX plots the outline of a box that is specified by its lower  
        left and upper right corner  
         
        Use as  
          ft_plot_box(position, ...)  
        where the position of the box is specified as is [x1, x2, y1, y2].  
         
        Optional arguments should come in key-value pairs and can include  
          'facealpha'     = transparency value between 0 and 1  
          'facecolor'     = color specification as [r g b] values or a string, for example 'brain', 'cortex', 'skin', 'red', 'r'  
          'edgecolor'     = color specification as [r g b] values or a string, for example 'brain', 'cortex', 'skin', 'red', 'r'  
          'parent'        = handle which is set as the parent for the plotted elements (default = [])  
          'tag'           = string, the tag assigned to the plotted elements (default = '')  
         
        It is possible to plot the object in a local pseudo-axis (c.f. subplot), which is specfied as follows  
          'hpos'          = horizontal position of the center of the local axes  
          'vpos'          = vertical position of the center of the local axes  
          'width'         = width of the local axes  
          'height'        = height of the local axes  
          'hlim'          = horizontal scaling limits within the local axes  
          'vlim'          = vertical scaling limits within the local axes  
          'parent'        = handle which is set as the parent for all plots (default = [])  
         
        Example  
          ft_plot_box([-1 1 2 3], 'facecolor', 'b')  
          axis([-4 4 -4 4])  
         
        See also FT_PLOT_LINE, FT_PLOT_CROSSHAIR  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/ft_plot_box.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_plot_box", *args, **kwargs)
