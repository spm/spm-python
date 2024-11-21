from spm.__wrapper__ import Runtime


def ft_volumereslice(*args, **kwargs):
    """
      FT_VOLUMERESLICE flips, permutes, interpolates and/or reslices a volume along the  
        principal axes of the coordinate system according to a specified resolution.  
         
        Use as  
          mri = ft_volumereslice(cfg, mri)  
        where the input MRI should be a single anatomical or functional MRI volume that  
        results from FT_READ_MRI or FT_VOLUMEREALIGN. You can visualize the the input and  
        output using FT_SOURCEPLOT.  
         
        The configuration structure can contain  
          cfg.method     = string, 'flip', 'nearest', 'linear', 'cubic' or 'spline' (default = 'linear')  
          cfg.downsample = integer number (default = 1, i.e. no downsampling)  
         
        If you specify the method as 'flip', it will only permute and flip the volume, but  
        not perform any interpolation. For the other methods the input volumetric data will  
        also be interpolated on a regular voxel grid.  
         
        For the interpolation methods you should specify  
          cfg.resolution = number, in units of distance (e.g. mm)  
          cfg.xrange     = [min max], in units of distance (e.g. mm)  
          cfg.yrange     = [min max], in units of distance (e.g. mm)  
          cfg.zrange     = [min max], in units of distance (e.g. mm)  
        or alternatively with  
          cfg.dim        = [nx ny nz], size of the volume in each direction  
         
        If the input MRI has a coordsys-field and you don't specify explicit the  
        xrange/yrange/zrange, the centre of the volume will be shifted (with respect to the  
        origin of the coordinate system), for the brain to fit nicely in the box.  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_VOLUMEREALIGN, FT_VOLUMEDOWNSAMPLE, FT_SOURCEINTERPOLATE, FT_SOURCEPLOT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_volumereslice.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_volumereslice", *args, **kwargs)
