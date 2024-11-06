from spm.__wrapper__ import Runtime


def ft_plot_text(*args, **kwargs):
    """
      FT_PLOT_TEXT helper function for plotting text, which can also be used in  
        combination with the multiple channel layout display in FieldTrip.  
         
        Use as  
          ft_plot_text(X, Y, str, ...)  
         
        Optional arguments should come in key-value pairs and can include  
          'fontcolor'           = string, color specification (default = 'k')  
          'fontsize'            = number, sets the size of the text (default = 10)  
          'fontunits'           =  
          'fontname'            =  
          'fontweight'          =  
          'horizontalalignment' =  
          'verticalalignment'   =  
          'interpreter'         = string, can be 'none', 'tex' or 'latex' (default = 'none')  
          'rotation'            =  
          'tag'                 = string, the tag assigned to the plotted elements (default = '')  
         
        It is possible to plot the object in a local pseudo-axis (c.f. subplot), which is specfied as follows  
          'hpos'                = horizontal position of the center of the local axes  
          'vpos'                = vertical position of the center of the local axes  
          'width'               = width of the local axes  
          'height'              = height of the local axes  
          'hlim'                = horizontal scaling limits within the local axes  
          'vlim'                = vertical scaling limits within the local axes  
         
        Example  
          figure  
          ft_plot_vector(randn(1,10), rand(1,10), 'hpos', 1, 'vpos', 1, 'width', 0.2, 'height', 0.2, 'box', true)  
          ft_plot_text(0, 0 , '+',                'hpos', 1, 'vpos', 1, 'width', 0.2, 'height', 0.2)  
          axis([0 2 0 2])  
         
        See also FT_PLOT_VECTOR, FT_PLOT_MATRIX, FT_PLOT_LINE, FT_PLOT_BOX  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/ft_plot_text.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_plot_text", *args, **kwargs)
