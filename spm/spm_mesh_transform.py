from spm.__wrap__ import _Runtime


def spm_mesh_transform(*args, **kwargs):
  """  Apply a spatial transformation to vertices of a surface mesh  
    FORMAT M = spm_mesh_transform(M,T,def)  
    M        - a patch structure or a gifti object or [nv x 3] array  
    T        - a [4 x 4] transformation matrix [default: identity]  
    def      - a deformation field (nifti object or filename) [default: none]  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_mesh_transform.m)
  """

  return _Runtime.call("spm_mesh_transform", *args, **kwargs)
