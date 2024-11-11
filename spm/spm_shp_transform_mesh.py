from spm.__wrapper__ import Runtime


def spm_shp_transform_mesh(*args, **kwargs):
    """
      Apply a transformation field to a mesh  
         
        FORMAT wf = spm_shp_transform_mesh(f, iy, [M])  
         
        f  - (gifti)            - Input mesh  
        iy - (Nx x Ny x Nz x 3) - Transformation   
        M  - (4 x 4)            - Voxel-to-world matrix of the transformation  
        wf - (gifti)            - Warped mesh (gifti object)  
         
        FORMAT wf = spm_shp_transform_mesh(f, T, [iy], [M])  
         
        T  - (4 x 4) Affine transformation to apply to the mesh beforehand.  
         
        * The transformation (iy) should be expressed in millimetres, that is,  
          each voxel contains a millimetric coordinate in world space.  
        * The voxel-to-world matrix (M) should map voxels to mm.  
        * The affine transformation matrix (T) should map mm to mm.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_shp_transform_mesh.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_shp_transform_mesh", *args, **kwargs)
