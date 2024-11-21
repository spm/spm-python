from spm.__wrapper__ import Runtime


def spm_eeg_inv_transform_mesh(*args, **kwargs):
    """
      Apply affine transformation to surface mesh  
        FORMAT mesh = spm_eeg_inv_transform_mesh(M, mesh)  
         
        M           - affine transformation matrix [4 x 4]  
        mesh        - patch structure  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_transform_mesh.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_inv_transform_mesh", *args, **kwargs)
