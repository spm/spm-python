from spm._runtime import Runtime


def spm_shp_project_velocity(*args, **kwargs):
    r"""
      Project a velocity (= a 4D volume) onto a subspace (= a 5D volume) to  
        compute its latent code (a 1D vector).  
         
        FORMAT z = spm_shp_project_velocity(v, [fmodel], [fsubspace])  
         
        v         - (Nx x Ny x Nz x 3) Initial velocity  
        fmodel    - Path to the model parameters  
                    [spm('Dir')/tpl/shp/model_variables.mat]  
        fsubspace - Path to the scaled subspace   
                    [spm('Dir')/tpl/shp/subspace_scaled.nii]  
        z         - (M x 1) Latent code  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_shp_project_velocity.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_shp_project_velocity", *args, **kwargs)
