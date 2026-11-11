from spm._runtime import Runtime


def ft_plot_headmodel(*args, **kwargs):
    r"""
      FT_PLOT_HEADMODEL visualizes the boundaries in the volume conduction model of the  
        head as specified in the headmodel structure. This works for any of the head models  
        supported by FieldTrip. For spherical models, it will construct and plot a  
        triangulated sphere.  
         
        Use as  
          ft_plot_headmodel(headmodel, ...)  
         
        Optional arguments should come in key-value pairs and can include  
          'facecolor'       = [r g b] values or string, for example 'skin', 'skull', 'brain', 'black', 'red', 'r', or an Nx3 or Nx1 array where N is the number of faces  
          'facealpha'       = transparency, between 0 and 1 (default = 1)  
          'faceindex'       = true or false  
          'vertexcolor'     = [r g b] values or string, for example 'skin', 'skull', 'brain', 'black', 'red', 'r', or an Nx3 or Nx1 array where N is the number of vertices  
          'vertexindex'     = true or false  
          'edgecolor'       = [r g b] values or string, for example 'skin', 'skull', 'brain', 'black', 'red', 'r'  
          'edgealpha'       = transparency, between 0 and 1 (default = 1)  
          'cutlocation'     = 1x3 vector specifying a point on the plane that cuts the mesh  
          'cutorientation'  = 1x3 vector specifying the direction orthogonal through the plane that cuts the mesh  
          'surfaceonly'     = true or false, plot only the outer surface of a hexahedral or tetrahedral mesh (default = false)  
          'unit'            = string, convert to the specified geometrical units (default = [])  
          'axes'            = boolean, whether to plot the axes of the 3D coordinate system (default = false)  
          'grad'            = gradiometer array, used in combination with local spheres model  
         
        Example  
          headmodel   = [];  
          headmodel.r = [86 88 92 100];  
          headmodel.o = [0 0 40];  
          figure  
          ft_plot_headmodel(headmodel);  
         
        See also FT_PREPARE_HEADMODEL, FT_DATATAYPE_HEADMODEL, FT_PLOT_MESH,  
        FT_PLOT_HEADSHAPE, FT_PLOT_SENS, FT_PLOT_DIPOLE, FT_PLOT_ORTHO, FT_PLOT_TOPO3D  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/plotting/ft_plot_headmodel.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_plot_headmodel", *args, **kwargs, nargout=0)
