from spm.__wrapper__ import Runtime


def ft_select_point3d(*args, **kwargs):
    """
      FT_SELECT_POINT3D helper function for selecting one or multiple points on a 3D mesh  
        using the mouse. It returns a list of the [x y z] coordinates of the selected  
        points.  
         
        Use as  
          [selected] = ft_select_point3d(bnd, ...)  
         
        Optional input arguments should come in key-value pairs and can include  
          'multiple'    = true/false, make multiple selections, pressing "q" on the keyboard finalizes the selection (default = false)  
          'nearest'     = true/false (default = true)  
          'marker'      = character or empty, for example '.', 'o' or 'x' (default = [])  
          'markersize'  = scalar, the size of the marker (default = 10)  
          'markercolor' = character, for example 'r', 'b' or 'g' (default = 'k')  
         
        Example  
          [pos, tri] = mesh_sphere(162);  
          bnd.pos = pos;  
          bnd.tri = tri;  
          ft_plot_mesh(bnd)  
          camlight  
          ... do something here  
         
        See also FT_SELECT_BOX, FT_SELECT_CHANNEL, FT_SELECT_POINT, FT_SELECT_RANGE, FT_SELECT_VOXEL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/ft_select_point3d.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_select_point3d", *args, **kwargs)
