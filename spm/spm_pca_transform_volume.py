from spm.__wrapper__ import Runtime


def spm_pca_transform_volume(*args, **kwargs):
  """  FORMAT wf = transform_volume(f, y, [itrp], [bnd])  
      f    - Input volume [Nx Ny Nz ...]  
      y    - Transformation [Mx My Mz 3]  
      itrp - Interpolation order {default: 1}  
      bnd  - Boundary conditions {default: 0 = no wrapping around}  
      wf   - Warped volume [Mx My Mz ...]  
     
    Note that the transformation must map two voxel spaces, so it should have  
    already been composed with voxel-to-world affine matrices.  
    Yael Balbastre 2024  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_pca_transform_volume.m)
  """

  return Runtime.call("spm_pac_transform_volume", *args, **kwargs)
