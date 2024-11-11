from spm.__wrapper__ import Runtime


def spm_shp_sample_deformation(*args, **kwargs):
    """
      FORMAT [iy,y,z] = spm_shp_sample_deformation(z,U,v0,z0)  
         
        z  - (M x 1) Latent code [NaN]   
                     NaN values will be sampled from the distribution   
        U  - Path to the scaled subspace [spm('Dir')/tpl/shp/subspace_scaled.nii]  
        v0 - (Nx x Ny x Nz x 3) Original velocity field [zero]  
        z0 - (Nx x Ny x Nz x 3) Original latent code    [zero]  
        iy - (Nx x Ny x Nz x 3) Inverse deformation (used to deform meshes)  
        y  - (Nx x Ny x Nz x 3) Forward deformation (used to deform volumes)  
         
        This function:  
        1. Samples z values from the standard distribution (if nonfinite input)  
        2. Generates the velocity field v = v0 + U * (z - z0)  
        3. Exponentiates the forward and inverse deformation fields iy and y  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_shp_sample_deformation.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_shp_sample_deformation", *args, **kwargs)
