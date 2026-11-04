from spm._runtime import Runtime


def ft_select_point(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/plotting/ft_select_point.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_select_point", *args, **kwargs)
