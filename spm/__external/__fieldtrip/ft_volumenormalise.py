from spm.__wrapper__ import Runtime


def ft_volumenormalise(*args, **kwargs):
    """
      FT_VOLUMENORMALISE normalises anatomical and functional volume data  
        to a template anatomical MRI.  
         
        Use as  
          [mri] = ft_volumenormalise(cfg, mri)  
        where the input mri should be a single anatomical volume that was for  
        example read with FT_READ_MRI.  
         
        The configuration options can be  
          cfg.parameter        = cell-array with the functional data to be normalised (default = 'all')  
          cfg.keepinside       = 'yes' or 'no', keep the inside/outside labeling (default = 'yes')  
          cfg.downsample       = integer number (default = 1, i.e. no downsampling)  
          cfg.spmversion       = string, 'spm2', 'spm8', 'spm12' (default = 'spm12')  
          cfg.spmmethod        = 'old', 'new' or 'mars', to switch between the different  
                                 spm12 implementations. The methods 'new' or 'mars'  
                                 uses SPM tissue probability maps instead of the  
                                 template MRI specified in cfg.template.  
          cfg.opts             = structure with normalisation options, see SPM documentation for details  
          cfg.template         = string, filename of the template anatomical MRI (default = 'T1.mnc'  
                                 for spm2 or 'T1.nii' for spm8 and for spm12).  
          cfg.templatecoordsys = the coordinate system of the template when using a template other  
                                 than the default  
          cfg.templatemask     = string, filename of a mask for the template  
                                 anatomical MRI spcified in cfg.template, e.g. a  
                                 brain mask (optional).  
          cfg.tpm              = string, file name of the SPM tissue probablility map to use in  
                                 case spmversion is 'spm12' and spmmethod is 'new' or 'mars'  
          cfg.write            = 'yes' or 'no' (default = 'no'), writes the segmented volumes to SPM2  
                                 compatible analyze-file, with the suffix  
                                 _anatomy for the anatomical MRI volume  
                                 _param   for each of the functional volumes  
          cfg.name             = string for output filename  
          cfg.keepintermediate = 'yes' or 'no' (default = 'no')  
          cfg.intermediatename = string, prefix of the the coregistered images and of the original  
                                 images in the original headcoordinate system  
          cfg.nonlinear        = 'yes' (default) or 'no', estimates a nonlinear transformation  
                                 in addition to the linear affine registration. If a reasonably  
                                 accurate normalisation is sufficient, a purely linearly transformed  
                                 image allows for 'reverse-normalisation', which might come in handy  
                                 when for example a region of interest is defined on the normalised  
                                 group-average  
          cfg.spmparams        = you can feed in the parameters from a prior normalisation, for example  
                                 to apply the parameters determined from an aantomical MRI to an  
                                 interpolated source resontruction  
          cfg.initial          = optional hard-coded alignment between target and template, the default is  
                                 to use FT_CONVERT_COORDSYS to estimate it based on the data (default = [])  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_READ_MRI, FT_VOLUMEDOWNSAMPLE, FT_SOURCEINTERPOLATE, FT_SOURCEPLOT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_volumenormalise.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_volumenormalise", *args, **kwargs)
