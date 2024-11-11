from spm.__wrapper__ import Runtime


def ft_volumedownsample(*args, **kwargs):
    """
      FT_VOLUMEDOWNSAMPLE downsamples, or more precisely decimates an anatomical MRI or  
        source reconstruction and optionally normalizes its coordinate axes, keeping the  
        homogenous transformation matrix correct.  
         
        Use as  
          [downsampled] = ft_volumedownsample(cfg, data)  
        where the input data structure should be an anatomical MRI that was for example  
        read with FT_READ_MRI or should be a volumetric source reconstruction from  
        FT_SOURCEANALYSIS or FT_SOURCEINTERPOLATE.  
         
        The configuration can contain  
          cfg.downsample = integer number (default = 1, i.e. no downsampling)  
          cfg.parameter  = string, data field to downsample (default = 'all')  
          cfg.smooth     = 'no' or the FWHM of the gaussian kernel in voxels (default = 'no')  
          cfg.keepinside = 'yes' or 'no', keep the inside/outside labeling (default = 'yes')  
          cfg.spmversion = string, 'spm2', 'spm8', 'spm12' (default = 'spm12')  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_SOURCEINTERPOLATE, FT_VOLUMEWRITE and FT_VOLUMENORMALISE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_volumedownsample.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_volumedownsample", *args, **kwargs)
