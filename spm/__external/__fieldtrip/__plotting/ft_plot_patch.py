from spm.__wrapper__ import Runtime


def ft_plot_patch(*args, **kwargs):
    """
      FT_PLOT_PATCH plot a colored shape, similar to the MATLAB patch() function. It is  
        similar in usage as ft_plot_vector, and they can be combined, for example,  
        to plot an area equivalent to a SEM or STD-DEV around a line.  
         
        Use as  
          ft_plot_patch(X, Y, ...)  
        where X and Y are similar as the input to the MATLAB patch() function.  
         
        Optional arguments should come in key-value pairs and can include  
          'axis'            = draw the local axis,  can be 'yes', 'no', 'xy', 'x' or 'y'  
          'parent'          = handle which is set as the parent for the plotted elements (default = [])  
          'tag'             = string, the tag assigned to the plotted elements (default = '')  
          'facecolor'       = see MATLAB standard patch properties  
          'facealpha'       = see MATLAB standard patch properties (note, approx. transparency can be achieved using 'facecolor')  
          'edgecolor'       = see MATLAB standard patch properties (default is 'none') (equivalent to 'linecolor' in PLOT)  
          'linestyle'       = see MATLAB standard patch properties  
          'linewidth'       = see MATLAB standard patch properties  
         
        The color of the patchand the edges (i.e. border lines) can be specified in a variety of ways  
          - as a string with one character per line that you want to plot. Supported colors are the same as in PATCH, i.e. 'bgrcmykw'.  
          - as an 'RGB triplet', a 1x3 vector with values between 0 and 1  
          - as 'none' if you do not want the face of the patch to be filled (useful when you want to plot an empty box).  
         
        It is possible to plot the object in a local pseudo-axis (c.f. subplot), which is specfied as follows  
          'box'             = draw a box around the local axes, can be 'yes' or 'no'  
          'hpos'            = horizontal position of the center of the local axes  
          'vpos'            = vertical position of the center of the local axes  
          'width'           = width of the local axes  
          'height'          = height of the local axes  
          'hlim'            = horizontal scaling limits within the local axes  
          'vlim'            = vertical scaling limits within the local axes  
         
        Example  
          hdat = [1:10 10:-1:1];  
          vdat = rand(1,10);  
          vdat = [vdat vdat(end:-1:1)+1];  
          ft_plot_patch(hdat, vdat)  
         
        See also FT_PLOT_VECTOR, PATCH, PLOT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/ft_plot_patch.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_plot_patch", *args, **kwargs)
