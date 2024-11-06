from spm.__wrapper__ import Runtime


def ft_select_point(*args, **kwargs):
    """
      FT_SELECT_POINT helper function for selecting a one or multiple points in the  
        current figure using the mouse. It returns a list of the [x y] coordinates of the  
        selected points.  
         
        Use as  
          [selected] = ft_select_point(pos, ...)  
         
        Optional input arguments should come in key-value pairs and can include  
          'multiple'   = true/false, make multiple selections, pressing "q" on the keyboard finalizes the selection (default = false)  
          'nearest'    = true/false (default = true)  
         
        Example  
          pos = randn(10,2);  
          figure  
          plot(pos(:,1), pos(:,2), '.')  
          ft_select_point(pos)  
         
        See also FT_SELECT_BOX, FT_SELECT_CHANNEL, FT_SELECT_POINT3D, FT_SELECT_RANGE, FT_SELECT_VOXEL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/ft_select_point.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_select_point", *args, **kwargs)
