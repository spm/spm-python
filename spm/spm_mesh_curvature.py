from spm.__wrapper__ import Runtime


def spm_mesh_curvature(*args, **kwargs):
  """  Compute a crude approximation of the curvature of a surface mesh  
    FORMAT C = spm_mesh_curvature(M)  
    M        - a patch structure  
     
    C        - curvature vector  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_mesh_curvature.m)
  """

  return Runtime.call("spm_mesh_curvature", *args, **kwargs)
