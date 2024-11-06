from spm.__wrapper__ import Runtime


def spm_uw_apply(*args, **kwargs):
    """
      Reslice images volume by volume  
        FORMAT spm_uw_apply(ds,[flags])  
        or  
        FORMAT P = spm_uw_apply(ds,[flags])  
         
         
        ds       - a structure created by spm_uw_estimate.m containing the fields:  
                   ds can also be an array of structures, each struct corresponding  
                   to one session (it hardly makes sense to try and pool fields across  
                   sessions since there will have been a reshimming). In that case each  
                   session is unwarped separately, unwarped into the distortion space of  
                   the average (default) position of that series, and with the first  
                   scan on the series defining the pahse encode direction. After that each  
                   scan is transformed into the space of the first scan of the first series.  
                   Naturally, there is still only one actual resampling (interpolation).  
                   It will be assumed that the same unwarping parameters have been used  
                   for all sessions (anything else would be truly daft).  
         
        .P           - Images used when estimating deformation field and/or  
                       its derivative w.r.t. modelled factors. Note that this  
                       struct-array may contain .mat fields that differ from  
                       those you would observe with spm_vol(P(1).fname). This  
                       is because spm_uw_estimate has an option to re-estimate  
                       the movement parameters. The re-estimated parameters are  
                       not written to disc (in the form of .mat files), but rather  
                       stored in the P array in the ds struct.  
         
        .order       - Number of basis functions to use for each dimension.  
                       If the third dimension is left out, the order for  
                       that dimension is calculated to yield a roughly  
                       equal spatial cut-off in all directions.  
                       Default: [8 8 *]  
        .sfP         - Static field supplied by the user. It should be a  
                       filename or handle to a voxel-displacement map in  
                       the same space as the first EPI image of the time-  
                       series. If using the FieldMap toolbox, realignment  
                       should (if necessary) have been performed as part of  
                       the process of creating the VDM. Note also that the  
                       VDM mut be in undistorted space, i.e. if it is  
                       calculated from an EPI based field-map sequence  
                       it should have been inverted before passing it to  
                       spm_uw_estimate. Again, the FieldMap toolbox will  
                       do this for you.  
        .regorder    - Regularisation of derivative fields is based on the  
                       regorder'th (spatial) derivative of the field.  
                       Default: 1  
        .lambda      - Fudge factor used to decide relative weights of  
                       data and regularisation.  
                       Default: 1e5  
        .fot         - List of indexes for first order terms to model  
                       derivatives for. Order of parameters as defined  
                       by spm_imatrix.  
                       Default: [4 5]  
        .sot         - List of second order terms to model second  
                       derivatives of. Should be an nx2 matrix where  
                       e.g. [4 4; 4 5; 5 5] means that second partial  
                       derivatives of rotation around x- and y-axis  
                       should be modelled.  
                       Default: []  
        .fwhm        - FWHM (mm) of smoothing filter applied to images prior  
                       to estimation of deformation fields.  
                       Default: 6  
        .rem         - Re-Estimation of Movement parameters. Set to unity means  
                       that movement-parameters should be re-estimated at each  
                       iteration.  
                       Default: 0  
        .noi         - Maximum number of Iterations.  
                       Default: 5  
        .exp_round   - Point in position space to do Taylor expansion around.  
                       'First', 'Last' or 'Average'.  
        .p0          - Average position vector (three translations in mm  
                       and three rotations in degrees) of scans in P.  
        .q           - Deviations from mean position vector of modelled  
                       effects. Corresponds to deviations (and deviations  
                       squared) of a Taylor expansion of deformation fields.  
        .beta        - Coeffeicents of DCT basis functions for partial  
                       derivatives of deformation fields w.r.t. modelled  
                       effects. Scaled such that resulting deformation  
                       fields have units mm^-1 or deg^-1 (and squares  
                       thereof).  
        .SS          - Sum of squared errors for each iteration.  
         
        flags    - a structure containing various options.  The fields are:  
         
                jm   - Jacobian Modulation. If set, intensity (Jacobian)  
                       deformations are included in the model. If zero,  
                       intensity deformations are not considered.  
                      0   - Do only unwarping (not correcting  
                            for changing sampling density).  
                      1   - Do both unwarping and Jacobian correction.  
         
                mask - mask output images (1 for yes, 0 for no)  
                       To avoid artifactual movement-related variance the realigned  
                       set of images can be internally masked, within the set (i.e.  
                       if any image has a zero value at a voxel than all images have  
                       zero values at that voxel).  Zero values occur when regions  
                       'outside' the image are moved 'inside' the image during  
                       realignment.  
         
                mean - write mean image  
                       The average of all the realigned scans is written to  
                       mean*.<ext>.  
         
                interp - the interpolation method (see e.g. spm_bsplins.m).  
         
                which - Values of 0 or 1 are allowed.  
                        0   - don't create any resliced images.  
                              Useful if you only want a mean resliced image.  
                        1   - reslice all the images.  
         
                prefix - Filename prefix for resliced image files. Defaults to 'u'.  
         
                    The spatially realigned images are written to the original  
                    subdirectory with the same filename but prefixed with an 'u'.  
                    They are all aligned with the first.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_uw_apply.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_uw_apply", *args, **kwargs)
