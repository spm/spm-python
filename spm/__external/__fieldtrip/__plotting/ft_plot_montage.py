from spm.__wrapper__ import Runtime


def ft_plot_montage(*args, **kwargs):
    """
      FT_PLOT_MONTAGE makes a montage of a 3-D array by selecting slices at regular distances  
        and combining them in one large 2-D image.  Note that the montage of MRI slices is not to  
        be confused with the EEG montage, which is a way of specifying the reference scheme  
        between electrodes.  
         
        Use as  
          ft_plot_montage(dat, ...)  
        where dat is a 3-D array.  
          
        Additional options should be specified in key-value pairs and can be  
          'transform'     = 4x4 homogeneous transformation matrix specifying the mapping from voxel space to the coordinate system in which the data are plotted.  
          'location'      = 1x3 vector specifying a point on the plane which will be plotted, the coordinates are expressed in the coordinate system in which the data will be plotted. location defines the origin of the plane  
          'orientation'   = 1x3 vector specifying the direction orthogonal through the plane which will be plotted (default = [0 0 1])  
          'srange'        =   
          'slicesize'     =   
          'nslice'        = scalar, number of slices  
          'maskstyle'     = string, 'opacity' or 'colormix', defines the rendering  
          'background'    = needed when maskstyle is 'colormix', 3D-matrix with  
                            the same size as the data matrix, serving as  
                            grayscale image that provides the background  
          
        See also FT_PLOT_ORTHO, FT_PLOT_SLICE, FT_SOURCEPLOT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/ft_plot_montage.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_plot_montage", *args, **kwargs, nargout=0)
