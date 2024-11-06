from spm.__wrapper__ import Runtime


def ft_plot_crosshair(*args, **kwargs):
    """
      FT_PLOT_CROSSHAIR plots a crosshair at a specified position in two [x, y] or three  
        [x, y, z] dimensions.  
         
        Use as  
          h = ft_plot_crosshair(pos, ...)  
        where pos is the desired position of the crosshair. The handles of the lines are  
        returned.  
         
        Optional input arguments should be specified in key-value pairs and can include  
          'color'    = [r g b] value or string, see PLOT  
          'parent'   = handle which is set as the parent for the plotted elements (default = [])  
          'handle'   = handle of the existing line objects to be updated  
         
        You can specify the handles of existing line objects which will be then updated,  
        rather than creating a new set of lines. If both parent and handle ar specified,  
        the handle option prevail.  
         
        Example  
          ft_plot_crosshair([0.5 0.5], 'color', 'r')  
         
        See also FT_PLOT_BOX, FT_PLOT_LINE, TEXT, LINE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/ft_plot_crosshair.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_plot_crosshair", *args, **kwargs)
