from spm.__wrapper__ import Runtime


def FieldMap(*args, **kwargs):
    """
      FieldMap is an SPM Toolbox for creating field maps and unwarping EPI.  
        A full description of the toolbox and a usage manual can be found in  
        FieldMap.md. This can launched by the toolbox help button or using  
        `spm_help FieldMap.md`. The theoretical and practical principles behind  
        the toolbox are described in FieldMap_principles.md.  
         
        FORMAT FieldMap  
         
        FieldMap launches the GUI-based toolbox. Help is available via the help  
        button (which calls spm_help FieldMap.md). FieldMap is a multi function  
        function so that the toolbox routines can also be accessed without using  
        the GUI. A description of how to do this can be found in FieldMap_ngui.m  
         
        Input parameters and the mode in which the toolbox works can be  
        customised using the defaults file called pm_defaults.m.  
         
        Main data structure:  
         
        IP.P              : 4x1 cell array containing real part short TE,  
                            imaginary part short TE, real part long TE and  
                            imaginary part long TE.  
        IP.pP             : Cell containing pre-calculated phase map. N.B.  
                            IP.P and IP.pP are mutually exclusive.  
        IP.epiP           : Cell containing EPI image used to demonstrate  
                            effects of unwarping.  
        IP.fmagP          : Cell containing fieldmap magnitude image used for  
                            coregistration  
        IP.wfmagP         : Cell containing forward warped fieldmap magnitude  
                            image used for coregistration  
        IP.uepiP          : Cell containing unwarped EPI image.  
        IP.nwarp          : Cell containing non-distorted image.  
        IP.vdmP           : Cell containing the voxel displacement map (VDM)  
        IP.et             : 2x1 Cell array with short and long echo-time (ms).  
        IP.epifm          : Flag indicating EPI based field map (1) or not (0).  
        IP.blipdir        : Direction of phase-encode blips for k-space traversal  
                           (1 = positive or -1 = negative)  
        IP.ajm            : Flag indicating if Jacobian modulation should be applied  
                           (1) or not (0).  
        IP.tert           : Total epi readout time (ms).  
        IP.maskbrain      : Flag indicating whether to mask the brain for fieldmap creation  
        IP.uflags         : Struct containing parameters guiding the unwrapping.  
                            Further explanations of these parameters are in  
                            FieldMap.md and pm_make_fieldmap.m  
        .iformat          : 'RI' or 'PM'  
        .method           : 'Huttonish', 'Mark3D' or 'Mark2D'  
        .fwhm             : FWHM (mm) of Gaussian filter for field map smoothing  
        .pad              : Size (in-plane voxels) of padding kernel.  
        .etd              : Echo time difference (ms).  
        .bmask  
         
        IP.mflags         : Struct containing parameters for brain maskin  
        .template         : Name of template for segmentation.  
        .fwhm             : fwhm of smoothing kernel for generating mask.  
        .nerode           : number of erosions  
        .ndilate          : number of dilations  
        .thresh           : threshold for smoothed mask.  
        .reg              : bias field regularisation  
        .graphics         : display or not  
         
        IP.fm             : Struct containing field map information  
        IP.fm.upm         : Phase-unwrapped field map (Hz).  
        IP.fm.mask        : Binary mask excluding the noise in the phase map.  
        IP.fm.opm         : "Raw" field map (Hz) (not unwrapped).  
        IP.fm.fpm         : Phase-unwrapped, regularised field map (Hz).  
        IP.fm.jac         : Partial derivative of field map in y-direction.  
         
        IP.vdm            : Struct with voxel displacement map information  
        IP.vdm.vdm        : Voxel displacement map (scaled version of IP.fm.fpm).  
        IP.vdm.jac        : Jacobian-1 of forward transform.  
        IP.vdm.ivdm       : Inverse transform of voxel displacement  
                            (used to unwarp EPI image if field map is EPI based)  
                            (used to warp flash image prior to coregistration  
                            when field map is flash based (or other T2 weighting).  
        IP.vdm.ijac       : Jacobian-1 of inverse transform.  
        IP.jim            : Jacobian sampled in space of EPI.  
         
        IP.cflags         : Struct containing flags for coregistration  
                            (these are the default SPM coregistration flags -  
                            defaults.coreg).  
        .cost_fun  
        .sep  
        .tol  
        .fwhm  
         
       __________________________________________________________________________  
        Refs and Background reading:  
         
        Jezzard P & Balaban RS. 1995. Correction for geometric distortion in  
        echo planar images from Bo field variations. MRM 34:65-73.  
         
        Hutton C et al. 2002. Image Distortion Correction in fMRI: A Quantitative  
        Evaluation, NeuroImage 16:217-240.  
         
        Cusack R & Papadakis N. 2002. New robust 3-D phase unwrapping  
        algorithms: Application to magnetic field mapping and  
        undistorting echoplanar images. NeuroImage 16:754-764.  
         
        Jenkinson M. 2003. Fast, automated, N-dimensional phase-  
        unwrapping algorithm. MRM 49:193-197.  
       __________________________________________________________________________  
        Acknowledegments:  
         
        Wellcome Trust and IBIM Consortium  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/FieldMap/FieldMap.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("FieldMap", *args, **kwargs)
