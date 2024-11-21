from spm.__wrapper__ import Runtime


def spm_uw_get_image_def(*args, **kwargs):
    """
      Estimation of deformation field (and optionally Jacobian field)   
        FORMAT [def] = spm_uw_get_image_def(i,ds,[defa])  
        or  
        FORMAT [def] = spm_uw_get_image_def(P,ds,[defa])  
        or  
        FORMAT [def,jac] = spm_uw_get_image_def(i,ds,[defa],[ddefa])  
        or  
        FORMAT [def,jac] = spm_uw_get_image_def(P,ds,[defa],[ddefa])  
         
         
        i          - Index into array of file handles given in ds.  
        P          - File-name or -handle of file that was acquired in same  
                     session as the files in ds.P. Note that P does not have to  
                     be one of the files used to estimate the partial derivatives  
                     of the deformation fields.  
        ds         - Structure returned by spm_uw_estimate.m  
        defa       - Array of partial derivative deformation fields scaled to  
                     mm^-1 or deg^-1 (or squares thereof).  
                     If not provided it will be calculated, but it can be a good  
                     idea to calculate it once and for all if one does repeated  
                     calls with the same ds.  
        ddefa      - Array of partial derivative in the phase encoding direction  
                     of partial derivatives (w.r.t. movement parameters) of  
                     deformation fields. Used when local Jacobians are to be  
                     estimated along with deformation fields.  
         
         
        def        - Deformation field for file given by P, or by ds.P(i).  
                     Add to xyz when calling spm_sample_vol.m  
        jac        - Field of determinants of local Jacobians, i.e. determinants  
                     of array of partial derivatives of for dx'/dx, dy'/dy,  
                     dy'/dx etc where x', y'... are transformed coordinates and  
                     x, y... are original coordinates.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_uw_get_image_def.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_uw_get_image_def", *args, **kwargs)
