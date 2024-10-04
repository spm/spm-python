from spm.__wrap__ import _Runtime


def spm_mesh_curvature(*args, **kwargs):
  """  Compute a crude approximation of the curvature of a surface mesh  
    FORMAT C = spm_mesh_curvature(M)  
    M        - a patch structure  
     
    C        - curvature vector  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_mesh_curvature.m)
  """

  return _Runtime.call("spm_mesh_curvature", *args, **kwargs)
