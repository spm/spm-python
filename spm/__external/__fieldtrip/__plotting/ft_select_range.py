from spm.__wrapper__ import Runtime


def ft_select_range(*args, **kwargs):
    """
      FT_SELECT_RANGE is a helper function that can be used as callback function  
        in a figure. It allows the user to select a horizontal or a vertical  
        range, or one or multiple boxes.  
         
        The callback function (and it's arguments) specified in callback is called  
        on a left-click inside a selection, or using the right-click context-menu.  
        The callback function will have as its first-to-last input argument the range of  
        all selections. The last input argument is either empty, or, when using the context  
        menu, a label of the item clicked.  
        Context menus are shown as the labels presented in the input. When activated,  
        the callback function is called, with the last input argument being the label of  
        the selection option.  
         
        Input arguments:  
          'event'       = string, event used as hook.  
          'callback'    = function handle or cell-array containing function handle and additional input arguments  
          'contextmenu' = cell-array containing labels shown in right-click menu  
          'multiple'    = boolean, allowing multiple selection boxes or not  
          'xrange'      = boolean, xrange variable or not  
          'yrange'      = boolean, yrange variable or not  
          'clear'       = boolean  
         
        Example  
          x = randn(10,1);  
          y = randn(10,1);  
          figure; plot(x, y, '.');  
         
        The following example allows multiple horizontal and vertical selections to be made  
          set(gcf, 'WindowButtonDownFcn',   {@ft_select_range, 'event', 'WindowButtonDownFcn',   'multiple', true, 'callback', @disp});  
          set(gcf, 'WindowButtonMotionFcn', {@ft_select_range, 'event', 'WindowButtonMotionFcn', 'multiple', true, 'callback', @disp});  
          set(gcf, 'WindowButtonUpFcn',     {@ft_select_range, 'event', 'WindowButtonUpFcn',     'multiple', true, 'callback', @disp});  
         
        The following example allows a single horizontal selection to be made  
          set(gcf, 'WindowButtonDownFcn',   {@ft_select_range, 'event', 'WindowButtonDownFcn',   'multiple', false, 'xrange', true, 'yrange', false, 'callback', @disp});  
          set(gcf, 'WindowButtonMotionFcn', {@ft_select_range, 'event', 'WindowButtonMotionFcn', 'multiple', false, 'xrange', true, 'yrange', false, 'callback', @disp});  
          set(gcf, 'WindowButtonUpFcn',     {@ft_select_range, 'event', 'WindowButtonUpFcn',     'multiple', false, 'xrange', true, 'yrange', false, 'callback', @disp});  
         
        The following example allows a single point to be selected  
          set(gcf, 'WindowButtonDownFcn',   {@ft_select_range, 'event', 'WindowButtonDownFcn',   'multiple', false, 'xrange', false, 'yrange', false, 'callback', @disp});  
          set(gcf, 'WindowButtonMotionFcn', {@ft_select_range, 'event', 'WindowButtonMotionFcn', 'multiple', false, 'xrange', false, 'yrange', false, 'callback', @disp});  
          set(gcf, 'WindowButtonUpFcn',     {@ft_select_range, 'event', 'WindowButtonUpFcn',     'multiple', false, 'xrange', false, 'yrange', false, 'callback', @disp});  
         
        See also FT_SELECT_BOX, FT_SELECT_CHANNEL, FT_SELECT_POINT, FT_SELECT_POINT3D, FT_SELECT_VOXEL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/ft_select_range.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_select_range", *args, **kwargs, nargout=0)
