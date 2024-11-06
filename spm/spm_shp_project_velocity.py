from spm.__wrapper__ import Runtime


def spm_shp_project_velocity(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_shp_project_velocity.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_shp_project_velocity", *args, **kwargs)
