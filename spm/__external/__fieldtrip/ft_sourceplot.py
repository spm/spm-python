from spm.__wrapper__ import Runtime


def ft_sourceplot(*args, **kwargs):
    """
      FT_SOURCEPLOT plots functional source reconstruction data on slices or on a surface,  
        optionally as an overlay on anatomical MRI data, where statistical data can be used to  
        determine the opacity of the mask. Input data comes from FT_SOURCEANALYSIS,  
        FT_SOURCEGRANDAVERAGE or statistical values from FT_SOURCESTATISTICS.  
         
        Use as  
          ft_sourceplot(cfg, anatomical)  
          ft_sourceplot(cfg, functional)  
          ft_sourceplot(cfg, functional, anatomical)  
        where the input data can contain either anatomical, functional or statistical data,  
        or a combination of them.  
         
        The input data can be in a 3-D volumetric representation or in a 2-D cortical sheet  
        representation.  If both anatomical and functional/statistical data is provided as input,  
        they should be represented in the same coordinate system or interpolated on the same  
        geometrical representation, e.g. using FT_SOURCEINTERPOLATE.  
         
        The slice and ortho visualization plot the data in the input data voxel arrangement, i.e.  
        the three ortho views are the 1st, 2nd and 3rd dimension of the 3-D data matrix, not of  
        the head coordinate system. The specification of the coordinate for slice intersection  
        is specified in head coordinates, i.e. relative to anatomical landmarks or fiducials and  
        expressed in mm or cm. If you want the visualisation to be consistent with the head  
        coordinate system, you can reslice the data using FT_VOLUMERESLICE. See http://bit.ly/1OkDlVF  
         
        The configuration should contain:  
          cfg.method        = 'ortho',      plots the data on three orthogonal slices  
                              'slice',      plots the data on a number of slices in the same plane  
                              'surface',    plots the data on a 3D brain surface  
                              'glassbrain', plots a max-projection through the brain  
                              'vertex',     plots the grid points or vertices scaled according to the functional value  
                              'cloud',      plot the data as clouds, spheres, or points scaled according to the functional value  
        and  
          cfg.anaparameter  = string, field in data with the anatomical data (default = 'anatomy' if present in data)  
          cfg.funparameter  = string, field in data with the functional parameter of interest (default = [])  
          cfg.maskparameter = string, field in the data to be used for opacity masking of fun data (default = [])  
                               If values are between 0 and 1, zero is fully transparant and one is fully opaque.  
                               If values in the field are not between 0 and 1 they will be scaled depending on the values  
                               of cfg.opacitymap and cfg.opacitylim (see below)  
                               You can use masking in several ways, f.i.  
                               - use outcome of statistics to show only the significant values and mask the insignificant  
                                 NB see also cfg.opacitymap and cfg.opacitylim below  
                               - use the functional data itself as mask, the highest value (and/or lowest when negative)  
                                 will be opaque and the value closest to zero transparent  
                               - Make your own field in the data with values between 0 and 1 to control opacity directly  
         
        The following parameters can be used in all methods:  
          cfg.downsample    = downsampling for resolution reduction, integer value (default = 1) (orig: from surface)  
          cfg.atlas         = string, filename of atlas to use (default = []) see FT_READ_ATLAS  
                               for ROI masking (see 'masking' below) or for orthogonal plots (see method='ortho' below)  
          cfg.visible       = string, 'on' or 'off' whether figure will be visible (default = 'on')  
          cfg.figure        = 'yes' or 'no', whether to open a new figure. You can also specify a figure handle from FIGURE, GCF or SUBPLOT. (default = 'yes')  
          cfg.position      = location and size of the figure, specified as [left bottom width height] (default is automatic)  
          cfg.renderer      = string, 'opengl', 'zbuffer', 'painters', see RENDERERINFO. The OpenGL renderer is required when using opacity (default = 'opengl')  
         
        The following parameters can be used for the functional data:  
          cfg.funcolormap   = colormap for functional data, see COLORMAP (default = 'auto')  
                              'auto', depends structure funparameter, or on funcolorlim  
                                - funparameter: only positive values, or funcolorlim:'zeromax' -> 'hot'  
                                - funparameter: only negative values, or funcolorlim:'minzero' -> 'cool'  
                                - funparameter: both pos and neg values, or funcolorlim:'maxabs' -> 'default'  
                                - funcolorlim: [min max] if min & max pos-> 'hot', neg-> 'cool', both-> 'default'  
          cfg.funcolorlim   = color range of the functional data (default = 'auto')  
                               [min max]  
                               'maxabs', from -max(abs(funparameter)) to +max(abs(funparameter))  
                               'zeromax', from 0 to max(funparameter)  
                               'minzero', from min(funparameter) to 0  
                               'auto', if funparameter values are all positive: 'zeromax',  
                                 all negative: 'minzero', both possitive and negative: 'maxabs'  
          cfg.colorbar      = 'yes' or 'no' (default = 'yes')  
          cfg.colorbartext  =  string indicating the text next to colorbar  
         
        The 'ortho' method can also plot time and/or frequency, the other methods can not.  
        If your functional data has a time and/or frequency dimension, you can use  
          cfg.latency       = scalar or string, can be 'all', 'prestim', 'poststim', or [beg end], specify time range in seconds  
          cfg.avgovertime   = string, can be 'yes' or 'no' (default = 'no')  
          cfg.frequency     = scalar or string, can be 'all', or [beg end], specify frequency range in Hz  
          cfg.avgoverfreq   = string, can be 'yes' or 'no' (default = 'no')  
         
        The following parameters can be used for the masking data:  
          cfg.maskstyle     = 'opacity', or 'colormix'. If 'opacity', low-level  
                                graphics opacity masking is applied, if  
                                'colormix', the color data is explicitly  
                                expressed as a single RGB value, incorporating  
                                the opacitymask. Yields faster and more robust  
                                rendering in general.  
          cfg.opacitymap    = opacitymap for mask data, see ALPHAMAP (default = 'auto')  
                              'auto', depends structure maskparameter, or on opacitylim  
                                - maskparameter: only positive values, or opacitylim:'zeromax' -> 'rampup'  
                                - maskparameter: only negative values, or opacitylim:'minzero' -> 'rampdown'  
                                - maskparameter: both pos and neg values, or opacitylim:'maxabs' -> 'vdown'  
                                - opacitylim: [min max] if min & max pos-> 'rampup', neg-> 'rampdown', both-> 'vdown'  
                                - NB. to use p-values use 'rampdown' to get lowest p-values opaque and highest transparent  
          cfg.opacitylim    = range of mask values to which opacitymap is scaled (default = 'auto')  
                               [min max]  
                               'maxabs', from -max(abs(maskparameter)) to +max(abs(maskparameter))  
                               'zeromax', from 0 to max(abs(maskparameter))  
                               'minzero', from min(abs(maskparameter)) to 0  
                               'auto', if maskparameter values are all positive: 'zeromax',  
                                 all negative: 'minzero', both positive and negative: 'maxabs'  
          cfg.roi           = string or cell of strings, region(s) of interest from anatomical atlas (see cfg.atlas above)  
                               everything is masked except for ROI  
         
        When cfg.method='ortho', three orthogonal slices will be rendered. You can click in any  
        of the slices to update the display in the other two. You can also use the arrow keys on  
        your keyboard to navigate in one-voxel steps. Note that the slices are along the first,  
        second and third voxel dimension, which do not neccessarily correspond to the axes of the  
        head coordinate system. See http://bit.ly/1OkDlVF  
         
        The following parameters apply when cfg.method='ortho'  
          cfg.location      = location of cut, (default = 'auto')  
                               'auto', 'center' if only anatomy, 'max' if functional data  
                               'min' and 'max' position of min/max funparameter  
                               'center' of the brain  
                               [x y z], coordinates in voxels or head, see cfg.locationcoordinates  
          cfg.locationcoordinates = coordinate system used in cfg.location, 'head' or 'voxel' (default = 'head')  
                                     'head', headcoordinates as mm or cm  
                                     'voxel', voxelcoordinates as indices  
          cfg.crosshair     = 'yes' or 'no' (default = 'yes')  
          cfg.axis          = 'on' or 'off' (default = 'on')  
          cfg.queryrange    = number, in atlas voxels (default = 1)  
          cfg.clim          = lower and upper anatomical MRI limits (default = [0 1])  
         
        When cfg.method='slice', a NxM montage with a large number of slices will be rendered.  
        All slices are evenly spaced and along the same dimension.  
         
        The following parameters apply for cfg.method='slice'  
          cfg.nslices       = number of slices, (default = 20)  
          cfg.slicerange    = range of slices in data, (default = 'auto')  
                              'auto', full range of data  
                              [min max], coordinates of first and last slice in voxels  
          cfg.slicedim      = dimension to slice 1 (x-axis) 2(y-axis) 3(z-axis) (default = 3)  
          cfg.title         = string, title of the plot  
          cfg.figurename    = string, title of the figure window  
         
        When cfg.method='surface', the functional data will be rendered onto a cortical mesh  
        (can be an inflated mesh). If the input source data contains a tri-field (i.e. a  
        description of a mesh), no interpolation is needed. If the input source data does not  
        contain a tri-field, an interpolation is performed onto a specified surface. Note that  
        the coordinate system in which the surface is defined should be the same as the coordinate  
        system that is represented in the pos-field.  
         
        The following parameters apply to cfg.method='surface' when an interpolation is required  
          cfg.surffile       = string, file that contains the surface (default = 'surface_white_both.mat')  
                               'surface_white_both.mat' contains a triangulation that corresponds with the  
                                SPM anatomical template in MNI coordinates  
          cfg.surfinflated   = string, file that contains the inflated surface (default = [])  
                               may require specifying a point-matching (uninflated) surffile  
          cfg.surfdownsample = number (default = 1, i.e. no downsampling)  
          cfg.projmethod     = projection method, how functional volume data is projected onto surface  
                               'nearest', 'project', 'sphere_avg', 'sphere_weighteddistance'  
          cfg.projvec        = vector (in mm) to allow different projections that  
                               are combined with the method specified in cfg.projcomb  
          cfg.projcomb       = 'mean', 'max', method to combine the different projections  
          cfg.projweight     = vector of weights for the different projections (default = 1)  
          cfg.projthresh     = implements thresholding on the surface level  
                               for example, 0.7 means 70% of maximum  
          cfg.sphereradius   = maximum distance from each voxel to the surface to be  
                               included in the sphere projection methods, expressed in mm  
          cfg.distmat        = precomputed distance matrix (default = [])  
         
        The following parameters apply to cfg.method='surface' irrespective of whether an interpolation is required  
          cfg.camlight       = 'yes' or 'no' (default = 'yes')  
          cfg.facecolor      = [r g b] values or string, for example 'brain', 'cortex', 'skin', 'black', 'red', 'r',  
                               or an Nx3 or Nx1 array where N is the number of faces  
          cfg.vertexcolor    = [r g b] values or string, for example 'brain', 'cortex', 'skin', 'black', 'red', 'r',  
                               or an Nx3 or Nx1 array where N is the number of vertices  
          cfg.edgecolor      = [r g b] values or string, for example 'brain', 'cortex', 'skin', 'black', 'red', 'r'  
         
        When cfg.method = 'cloud', the functional data will be rendered as as clouds (groups of points),   
        spheres, or single points at each sensor position. These spheres or point clouds can either be   
        viewed in 3D or as 2D slices. The 'anatomical' input may also consist of a single or multiple   
        triangulated surface meshes in an Nx1 cell-array to be plotted with the interpolated functional   
        data (see FT_PLOT_CLOUD).  
         
        The following parameters apply to cfg.method='cloud'  
          cfg.cloudtype       = 'point' plots a single point at each sensor position  
                                'cloud' (default) plots each a group of spherically arranged points at each sensor position  
                                'surf' plots a single spherical surface mesh at each sensor position  
          cfg.radius          = scalar, maximum radius of cloud (default = 4)  
          cfg.colorgrad       = 'white' or a scalar (e.g. 1), degree to which color of points in cloud  
                                changes from its center  
          cfg.slice           = requires 'anatomical' as input (default = 'none')  
                                '2d', plots 2D slices through the cloud with an outline of the mesh  
                                '3d', draws an outline around the mesh at a particular slice  
          cfg.ori             = 'x', 'y', or 'z', specifies the orthogonal plane which will be plotted (default = 'y')  
          cfg.slicepos        = 'auto' or Nx1 vector specifying the position of the  
                                slice plane along the orientation axis (default = 'auto': chooses slice(s) with  
                                the most data)  
          cfg.nslices         = scalar, number of slices to plot if 'slicepos' = 'auto (default = 1)  
          cfg.minspace        = scalar, minimum spacing between slices if nslices>1 (default = 1)  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
        If you specify this option the input data will be read from a *.mat file on  
        disk. This mat files should contain only a single variable corresponding to the  
        input structure.  
         
        See also FT_SOURCEMOVIE, FT_SOURCEANALYSIS, FT_SOURCEGRANDAVERAGE, FT_SOURCESTATISTICS,  
        FT_VOLUMELOOKUP, FT_READ_ATLAS, FT_READ_MRI  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_sourceplot.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_sourceplot", *args, **kwargs)
