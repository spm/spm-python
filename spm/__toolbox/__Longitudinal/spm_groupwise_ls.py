from spm.__wrapper__ import Runtime


def spm_groupwise_ls(*args, **kwargs):
    """
      Groupwise registration via least squares  
        FORMAT out = spm_groupwise_ls(Nii, output, prec, w_settings, b_settings, s_settings, ord)  
        Nii    - a nifti object for two or more image volumes.  
        output - a cell array of output options (as scharacter strings).  
                 'avg'   - return average in out.avg  
                 'wavg'  - write average to disk, and return filename in out.avg  
                 'def'   - return mappings from average to individuals in out.def  
                 'wdef'  - write mappings to disk, and return filename in out.def  
                 'div'   - return divergence of initial velocities in out.div  
                 'wdiv'  - write divergence images to disk and return filename  
                 'jac'   - return Jacobian determinant maps in out.jac  
                 'wjac'  - write Jacobians to disk and return filename  
                 'vel'   - return initial velocities  
                 'wvel'  - write velocities to disk and return filename  
                 'rigid' - return rigid-body transforms  
         
        prec       - reciprocal of noise variance on images.  
        w_swttings - regularisation settings for warping.  
        b_settings - regularisation settings for nonuniformity field.  
        s_settings - number of time steps for geodesic shooting.  
        ord        - degree of B-spline interpolation used for sampline images.  
         
        This function requires an obscene amount of memory.  If it crashes  
        with an "Out of memory" error, then do not be too surprised.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Longitudinal/spm_groupwise_ls.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_groupwise_ls", *args, **kwargs)
