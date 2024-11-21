from spm.__wrapper__ import Runtime


def spm_shp_transform_volume(*args, **kwargs):
    """
      FORMAT wf = spm_shp_transform_volume(f, y, [itrp], [bnd])  
         
        f    - Input volume [Nx Ny Nz ...]  
        y    - Transformation [Mx My Mz 3]  
        itrp - Interpolation order {default: 1}  
        bnd  - Boundary conditions {default: 0 = no wrapping around}  
        wf   - Warped volume [Mx My Mz ...]  
         
        This is a simple wrapper around spm_diffeo to transform volumes with  
        any number of channel dimensions.  
         
        Note that the transformation must map two voxel spaces, so it should have  
        already been composed with voxel-to-world affine matrices.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_shp_transform_volume.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_shp_transform_volume", *args, **kwargs)
