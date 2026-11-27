from spm._runtime import Runtime


def spm_eeg_inv_transform_mesh(*args, **kwargs):
    r"""
      Apply affine transformation to surface mesh  
        FORMAT mesh = spm_eeg_inv_transform_mesh(M, mesh)  
         
        M           - affine transformation matrix [4 x 4]  
        mesh        - patch structure  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_inv_transform_mesh.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_inv_transform_mesh", *args, **kwargs)
