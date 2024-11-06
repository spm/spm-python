from spm.__wrapper__ import Runtime


def spm_shp_get_transforms(*args, **kwargs):
    """
      Transform MRI to model space and compute its latent code  
         
        FORMAT spm_shp_get_transforms(path_mri,[folder_out],[folder_shp])  
         
        path_mri   - Path to input MRI  
        folder_out - Path to output folder (default: {input_folder}/PCA)  
        folder_shp - Path to template folder (default: {spm('Dir')}/tpm/shp)  
        z          - Latent vectors describing the space in which the MRI lives  
          
        The following files are written in folder_out:  
        * pca_{mri_name}.mat - Shape representation of the MRI  
                                  'z'   - Latent vector  
                                  'r2n' - Import to native affine transform  
                                  'n2r' - Native to import affine transform  
        *    {mri_name}.nii  - Copy of input MRI  
        *  v_{mri_name}.nii  - Initial velocity (in import space)  
        * iv_{mri_name}.nii  - Initial velocity (in group space)  
        *  y_{mri_name}.nii  - Import to group nonlinear transform  
        * iy_{mri_name}.nii  - Group to import nonlinear transform  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_shp_get_transforms.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_shp_get_transforms", *args, **kwargs)
