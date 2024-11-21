from spm.__wrapper__ import Runtime


def ft_plot_vector(*args, **kwargs):
    """
      FT_PLOT_VECTOR visualizes a vector as a line, similar to PLOT.  
         
        Use as  
          ft_plot_vector(Y, ...)  
        or as  
          ft_plot_vector(X, Y, ...)  
        where X and Y are similar as the input to the MATLAB plot function.  
         
        Optional arguments should come in key-value pairs and can include  
          'color'           = see MATLAB standard line properties and see below  
          'style'           = see MATLAB standard line properties  
          'linewidth'       = see MATLAB standard line properties  
          'markersize'      = see MATLAB standard line properties  
          'markerfacecolor' = see MATLAB standard line properties  
          'axis'            = draw the local axis,  can be 'yes', 'no', 'xy', 'x' or 'y'  
          'highlight'       = a logical vector of size Y, where 1 means that the corresponding values in Y are highlighted (according to the highlightstyle)  
          'highlightstyle'  = can be 'box', 'thickness', 'saturation', 'difference' (default='box')  
          'facecolor'       = color for the highlighted box/difference (default = [0.6 0.6 0.6])  
          'facealpha'       = transparency for the highlighted box/difference, between 0 and 1 (default = 1)  
          'parent'          = handle which is set as the parent for all plots (default = [])  
          'tag'             = string, the tag assigned to the plotted elements (default = '')  
         
        The line color can be specified in a variety of ways  
          - as a string with one character per line that you want to plot. Supported colors are the same as in PLOT, i.e. 'bgrcmykw'.  
          - as 'none' if you do not want the lines to be plotted (useful in combination with the difference highlightstyle).  
          - as a Nx3 matrix, where N=length(x), to use graded RGB colors along the line  
         
        It is possible to plot the object in a local pseudo-axis (c.f. subplot), which is specfied as follows  
          'box'             = draw a box around the local axes, can be 'yes' or 'no'  
          'hpos'            = horizontal position of the center of the local axes  
          'vpos'            = vertical position of the center of the local axes  
          'width'           = width of the local axes  
          'height'          = height of the local axes  
          'hlim'            = horizontal scaling limits within the local axes  
          'vlim'            = vertical scaling limits within the local axes  
         
        When using a local pseudo-axis, you can plot a label next to the data  
          'label'           = string, label to be plotted in the corner of the box  
          'labelpos'        = string, position for the label (default = 'upperleft')  
          'fontcolor'       = string, color specification (default = 'k')  
          'fontsize'        = number, sets the size of the text (default = 10)  
          'fontunits'       =  
          'fontname'        =  
          'fontweight'      =  
         
        Example 1  
          subplot(2,1,1); ft_plot_vector(1:100, randn(1,100), 'color', 'r')  
          subplot(2,1,2); ft_plot_vector(1:100, randn(1,100), 'color', rand(100,3))  
         
        Example 2  
          ft_plot_vector(randn(1,100), 'width', 0.9, 'height', 0.9, 'hpos', 0, 'vpos', 0, 'box', 'yes')  
          ft_plot_vector(randn(1,100), 'width', 0.9, 'height', 0.9, 'hpos', 1, 'vpos', 0, 'box', 'yes')  
          ft_plot_vector(randn(1,100), 'width', 0.9, 'height', 0.9, 'hpos', 0, 'vpos', 1, 'box', 'yes')  
         
        Example 3  
         x = 1:100; y = hann(100)';  
         subplot(3,1,1); ft_plot_vector(x, y, 'highlight', y>0.8, 'highlightstyle', 'box');  
         subplot(3,1,2); ft_plot_vector(x, y, 'highlight', y>0.8, 'highlightstyle', 'thickness');  
         subplot(3,1,3); ft_plot_vector(x, y, 'highlight', y>0.8, 'highlightstyle', 'saturation');  
         
        Example 4  
         x = 1:100; y = hann(100)'; ymin = 0.8*y; ymax = 1.2*y;  
         ft_plot_vector(x, [ymin; ymax], 'highlight', ones(size(y)), 'highlightstyle', 'difference', 'color', 'none');  
         ft_plot_vector(x, y);  
         
        Example 5  
         colormap hot;  
         rgb = colormap;  
         rgb = interp1(1:64, rgb, linspace(1,64,100));  
         ft_plot_vector(1:100, 'color', rgb);  
         
        See also FT_PLOT_MATRIX, PLOT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/ft_plot_vector.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_plot_vector", *args, **kwargs)
