from spm.__wrapper__ import Runtime


def spm_uw_estimate(*args, **kwargs):
    """
      Estimation of partial derivatives of EPI deformation fields  
         
        FORMAT [ds] = spm_uw_estimate((P),(par))  
         
        P            - List of file names or headers.  
        par          - Structure containing parameters governing the specifics  
                       of how to estimate the fields.  
        .M           - When performing multi-session realignment and Unwarp we  
                       want to realign everything to the space of the first  
                       image in the first time-series. M defines the space of  
                       that.  
        .order       - Number of basis functions to use for each dimension.  
                       If the third dimension is left out, the order for   
                       that dimension is calculated to yield a roughly  
                       equal spatial cut-off in all directions.  
                       Default: [12 12 *]  
        .sfP         - Static field supplied by the user. It should be a   
                       filename or handle to a voxel-displacement map in  
                       the same space as the first EPI image of the time-  
                       series. If using the FieldMap toolbox, realignment  
                       should (if necessary) have been performed as part of  
                       the process of creating the VDM. Note also that the  
                       VDM must be in undistorted space, i.e. if it is  
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
                       Default: 'Average'.  
        ds           - The returned structure contains the following fields  
        .P           - Copy of P on input.  
        .sfP         - Copy of sfP on input (if non-empty).  
        .order       - Copy of order on input, or default.  
        .regorder    - Copy of regorder on input, or default.  
        .lambda      - Copy of lambda on input, or default.  
        .fot         - Copy of fot on input, or default.  
        .sot         - Copy of sot on input, or default.  
        .fwhm        - Copy of fwhm on input, or default.  
        .rem         - Copy of rem on input, or default.  
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
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_uw_estimate.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_uw_estimate", *args, **kwargs)
