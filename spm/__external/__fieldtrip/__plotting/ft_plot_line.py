from spm.__wrapper__ import Runtime


def ft_plot_line(*args, **kwargs):
    """
      FT_PLOT_LINE helper function for plotting a line, which can also be used in  
        combination with the multiple channel layout display in FieldTrip.  
         
        Use as  
          ft_plot_line(X, Y, ...)  
         
        Optional arguments should come in key-value pairs and can include  
          'color'           =  
          'linestyle'       =  
          'linewidth'       =  
          'tag'             = string, the tag assigned to the plotted elements (default = '')  
         
        It is possible to plot the object in a local pseudo-axis (c.f. subplot), which is specfied as follows  
          'hpos'            = horizontal position of the center of the local axes  
          'vpos'            = vertical position of the center of the local axes  
          'width'           = width of the local axes  
          'height'          = height of the local axes  
          'hlim'            = horizontal scaling limits within the local axes  
          'vlim'            = vertical scaling limits within the local axes  
         
        See also FT_PLOT_BOX, FT_PLOT_CROSSHAIR  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/ft_plot_line.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_plot_line", *args, **kwargs)
