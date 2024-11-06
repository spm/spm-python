from spm.__wrapper__ import Runtime


def ft_sliceinterp(*args, **kwargs):
    """
      FT_SLICEINTERP plots a 2D-montage of source reconstruction and anatomical MRI  
        after these have been interpolated onto the same grid.  
         
        Use as  
          ft_sliceinterp(cfg, interp)  
             or  
          [rgbimage] = ft_sliceinterp(cfg, interp), rgbimage is the monatage image  
         
        where interp is the output of sourceinterpolate and cfg is a structure  
        with any of the following fields:  
         
        cfg.funparameter  = string with the functional parameter of interest (default = 'source')  
        cfg.maskparameter = parameter used as opacity mask (default = 'none')  
        cfg.clipmin       = value or 'auto' (clipping of source data)  
        cfg.clipmax       = value or 'auto' (clipping of source data)  
        cfg.clipsym       = 'yes' or 'no' (default) symmetrical clipping  
        cfg.colormap      = colormap for source overlay (default is jet(128))  
        cfg.colmin        = source value mapped to the lowest color (default = 'auto')  
        cfg.colmax        = source value mapped to the highest color (default = 'auto')  
        cfg.maskclipmin   = value or 'auto' (clipping of mask data)  
        cfg.maskclipmax   = value or 'auto' (clipping of mask data)  
        cfg.maskclipsym   = 'yes' or 'no' (default) symmetrical clipping  
        cfg.maskmap       = opacitymap for source overlay (default is linspace(0,1,128))  
        cfg.maskcolmin    = mask value mapped to the lowest opacity, i.e. completely transparent (default ='auto')  
        cfg.maskcolmin    = mask value mapped to the highest opacity, i.e. non-transparent (default = 'auto')  
        cfg.alpha         = value between 0 and 1 or 'adaptive' (default)  
        cfg.nslices       = integer value, default is 20  
        cfg.dim           = integer value, default is 3 (dimension to slice)  
        cfg.spacemin      = 'auto' (default) or integer (first slice position)  
        cfg.spacemax      = 'auto' (default) or integer (last slice position)  
        cfg.resample      = integer value, default is 1 (for resolution reduction)  
        cfg.rotate        = number of ccw 90 deg slice rotations (default = 0)  
        cfg.title         = optional title (default is '')  
        cfg.whitebg       = 'yes' or 'no' (default = 'yes')  
        cfg.flipdim       = flip data along the sliced dimension, 'yes' or 'no' (default = 'no')  
        cfg.marker        = [Nx3] array defining N marker positions to display  
        cfg.markersize    = radius of markers (default = 5);  
        cfg.markercolor   = [1x3] marker color in RGB (default = [1 1 1], i.e. white)  
        cfg.interactive   = 'yes' or 'no' (default), interactive coordinates and source values  
         
        if cfg.alpha is set to 'adaptive' the opacity of the source overlay  
        linearly follows the source value: maxima are opaque and minima are  
        transparent.  
         
        if cfg.spacemin and/or cfg.spacemax are set to 'auto' the sliced  
        space is automatically restricted to the evaluated source-space  
         
        if cfg.colmin and/or cfg.colmax are set to 'auto' the colormap is mapped  
        to source values the following way: if source values are either all  
        positive or all negative the colormap is mapped to from  
        min(source) to max(source). If source values are negative and positive  
        the colormap is symmetrical mapped around 0 from -max(abs(source)) to  
        +max(abs(source)).  
         
        If cfg.maskparameter specifies a parameter to be used as an opacity mask  
        cfg.alpha is not used. Instead the mask values are maped to an opacitymap  
        that can be specified using cfg.maskmap. The mapping onto that  
        opacitymap is controlled as for the functional data using the  
        corresponding clipping and min/max options.  
         
        if cfg.whitebg is set to 'yes' the function estimates the head volume and  
        displays a white background outside the head, which can save a lot of black  
        printer toner.  
         
        if cfg.interactive is set to 'yes' a button will be displayed for  
        interactive data evaluation and coordinate reading. After clicking the  
        button named 'coords' you can click on any position in the slice montage.  
        After clicking these coordinates and their source value are displayed in  
        a text box below the button. The coordinates correspond to indeces in the  
        input data array:  
         
          f = interp.source(coord_1,coord_2,coord_3)  
         
        The coordinates are not affected by any transformations used for displaying  
        the data such as cfg.dim, cfg.rotate,cfg.flipdim or cfg.resample.  
         
        See also FT_SOURCEANALYSIS, FT_VOLUMERESLICE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_sliceinterp.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_sliceinterp", *args, **kwargs)
