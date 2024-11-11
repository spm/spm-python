from spm.__wrapper__ import Runtime


def ft_plot_headmodel(*args, **kwargs):
    """
      FT_PLOT_HEADMODEL visualizes the boundaries in the volume conduction model of the  
        head as specified in the headmodel structure. This works for any of the head models  
        supported by FieldTrip. For spherical models, it will construct and plot a  
        triangulated sphere.  
         
        Use as  
          ft_plot_headmodel(headmodel, ...)  
         
        Optional arguments should come in key-value pairs and can include  
          'facecolor'    = [r g b] values or string, for example 'brain', 'cortex', 'skin', 'black', 'red', 'r', or an Nx3 or Nx1 array where N is the number of faces  
          'vertexcolor'  = [r g b] values or string, for example 'brain', 'cortex', 'skin', 'black', 'red', 'r', or an Nx3 or Nx1 array where N is the number of vertices  
          'edgecolor'    = [r g b] values or string, for example 'brain', 'cortex', 'skin', 'black', 'red', 'r'  
          'faceindex'    = true or false  
          'vertexindex'  = true or false  
          'facealpha'    = transparency, between 0 and 1 (default = 1)  
          'edgealpha'    = transparency, between 0 and 1 (default = 1)  
          'surfaceonly'  = true or false, plot only the outer surface of a hexahedral or tetrahedral mesh (default = false)  
          'unit'         = string, convert to the specified geometrical units (default = [])  
          'axes'         = boolean, whether to plot the axes of the 3D coordinate system (default = false)  
          'grad'         = gradiometer array, used in combination with local spheres model  
         
        Example  
          headmodel   = [];  
          headmodel.r = [86 88 92 100];  
          headmodel.o = [0 0 40];  
          figure  
          ft_plot_headmodel(headmodel)  
         
        See also FT_PREPARE_HEADMODEL, FT_DATATAYPE_HEADMODEL, FT_PLOT_MESH,  
        FT_PLOT_HEADSHAPE, FT_PLOT_SENS, FT_PLOT_DIPOLE, FT_PLOT_ORTHO, FT_PLOT_TOPO3D  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/ft_plot_headmodel.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_plot_headmodel", *args, **kwargs, nargout=0)
