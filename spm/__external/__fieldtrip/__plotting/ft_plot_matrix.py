from spm.__wrapper__ import Runtime


def ft_plot_matrix(*args, **kwargs):
    """
      FT_PLOT_MATRIX visualizes a matrix as an image, similar to IMAGESC.  
        The position, width and height can be controlled to allow multiple  
        matrices (i.e. channels) to be plotted in a topographic arrangement.  
         
        Use as  
          ft_plot_matrix(C, ...)  
        where C is a 2 dimensional MxN matrix, or  
          ft_plot_matrix(X, Y, C, ...)  
        where X and Y describe the 1xN horizontal and 1xM vertical axes  
        respectively.  
         
        Optional arguments should come in key-value pairs and can include  
          'clim'            = 1x2 vector with color limits (default is automatic)  
          'highlight'       = a logical matrix of size C, where 0 means that the corresponding values in C are highlighted according to the highlightstyle  
          'highlightstyle'  = can be 'saturation', 'opacity', 'outline' or 'colormix' (default = 'opacity')  
          'tag'             = string, the tag assigned to the plotted elements (default = '')  
         
        It is possible to plot the object in a local pseudo-axis (c.f. subplot), which is specfied as follows  
          'box'             = draw a box around the local axes, can be 'yes' or 'no'  
          'hpos'            = horizontal position of the center of the local axes  
          'vpos'            = vertical position of the center of the local axes  
          'width'           = width of the local axes  
          'height'          = height of the local axes  
          'hlim'            = horizontal scaling limits within the local axes  
          'vlim'            = vertical scaling limits within the local axes  
         
        When using a local pseudo-axis, you can plot a label next to the data  
          'label'           = string, label to be plotted at the upper left corner  
          'fontcolor'       = string, color specification (default = 'k')  
          'fontsize'        = number, sets the size of the text (default = 10)  
          'fontunits'       =  
          'fontname'        =  
          'fontweight'      =  
         
        Example  
          ft_plot_matrix(randn(30,50), 'width', 1, 'height', 1, 'hpos', 0, 'vpos', 0)  
         
        See also FT_PLOT_VECTOR, IMAGESC, SURF  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/ft_plot_matrix.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_plot_matrix", *args, **kwargs, nargout=0)
