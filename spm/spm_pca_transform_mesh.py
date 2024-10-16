from spm.__wrapper__ import Runtime


def spm_pca_transform_mesh(*args, **kwargs):
  """  FORMAT wf = transform_mesh(f, iy, [M])  
      f    - Input mesh (gifti object)  
      iy   - Transformation [Mx My Mz 3]  
      M    - Voxel-to-world matrix of the transformation {default: eye(4)}  
      wf   - Warped mesh (gifti object)  
     
    FORMAT wf = transform_mesh(f, T, [iy], [M])  
      T    - World-to-world transformation to apply to the mesh first.  
     
    . The transformation (iy) should be expressed in millimetres, that is,  
      each voxel contains a millimetric coordinate in world space.  
    . The voxel-to-world matrix (M) should map voxels to mm.  
    . The affine transformation matrix (T) should map mm to mm.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_pca_transform_mesh.m)
  """

  return Runtime.call("spm_pac_transform_mesh", *args, **kwargs)
