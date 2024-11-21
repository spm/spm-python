from spm.__wrapper__ import Runtime


def ft_plot_axes(*args, **kwargs):
    """
      FT_PLOT_AXES adds three axes of 150 mm and a 10 mm sphere at the origin to the  
        present 3-D figure. The axes and sphere are scaled according to the units of the  
        geometrical object that is passed to this function. Furthermore, when possible,  
        the axes labels will represent the anatomical labels corresponding to the  
        specified coordinate system.  
         
        Use as  
          ft_plot_axes(object)  
         
        Additional optional input arguments should be specified as key-value pairs  
        and can include  
          'unit'       = string, plot axes that are suitable for the specified geometrical units (default = [])  
          'axisscale'  = scaling factor for the reference axes and sphere (default = 1)  
          'coordsys'   = string, assume the data to be in the specified coordinate system (default = 'unknown')  
          'transform'  = empty or 4x4 homogenous transformation matrix (default = [])  
          'fontcolor'  = string, color specification (default = [1 .5 0], i.e. orange)  
          'fontsize'   = number, sets the size of the text (default is automatic)  
          'fontunits'  =  
          'fontname'   =  
          'fontweight' =  
          'tag'        = string, the tag assigned to the plotted elements (default = '')   
         
        See also FT_PLOT_SENS, FT_PLOT_MESH, FT_PLOT_ORTHO, FT_PLOT_HEADSHAPE, FT_PLOT_DIPOLE, FT_PLOT_HEADMODEL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/ft_plot_axes.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_plot_axes", *args, **kwargs, nargout=0)
