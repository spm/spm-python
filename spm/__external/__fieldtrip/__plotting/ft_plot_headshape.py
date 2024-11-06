from spm.__wrapper__ import Runtime


def ft_plot_headshape(*args, **kwargs):
    """
      FT_PLOT_HEADSHAPE visualizes the shape of a head from a variety of  
        acquisition system. Usually the head shape is measured with a  
        Polhemus tracker and some proprietary software (e.g. from CTF, BTi  
        or Yokogawa). The headshape and fiducials can be used for coregistration.  
        If present in the headshape, the location of the fiducials will also  
        be shown.  
         
        Use as  
          ft_plot_headshape(headshape, ...)  
        where the headshape is a structure obtained from FT_READ_HEADSHAPE.  
         
        Optional arguments should come in key-value pairs and can include  
          'facecolor'    = [r g b] values or string, for example 'brain', 'cortex', 'skin', 'black', 'red', 'r', or an Nx3 or Nx1 array where N is the number of faces  
          'facealpha'    = transparency, between 0 and 1 (default = 1)  
          'vertexcolor'  = [r g b] values or string, for example 'brain', 'cortex', 'skin', 'black', 'red', 'r', or an Nx3 or Nx1 array where N is the number of vertices  
          'vertexsize'   = scalar value specifying the size of the vertices (default = 10)  
          'transform'    = transformation matrix for the fiducials, converts MRI voxels into head shape coordinates  
          'unit'         = string, convert to the specified geometrical units (default = [])  
          'axes'         = boolean, whether to plot the axes of the 3D coordinate system (default = false)  
          'tag'          = string, the tag assigned to the plotted elements (default = '')   
         
        The sensor array can include an optional fid field with fiducials, which will also be plotted.  
          'fidcolor'     = [r g b] values or string, for example 'red', 'r', or an Nx3 or Nx1 array where N is the number of fiducials  
          'fidmarker'    = ['.', '*', '+',  ...]  
          'fidlabel'     = ['yes', 'no', 1, 0, 'true', 'false']  
         
        Example:  
          headshape = ft_read_headshape(filename);  
          ft_plot_headshape(headshape)  
         
        See also FT_PLOT_MESH, FT_PLOT_HEADMODEL, FT_PLOT_SENS, FT_PLOT_DIPOLE,  
        FT_PLOT_ORTHO, FT_PLOT_TOPO3D  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/ft_plot_headshape.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_plot_headshape", *args, **kwargs)
