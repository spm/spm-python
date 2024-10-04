from spm.__wrap__ import _Runtime


def spm_mesh_detect(*args, **kwargs):
  """  True for valid representation of a mesh  
    FORMAT s = spm_mesh_detect(F)  
    F        - variable to query: filename, vol structure, patch structure  
    s        - true if F corresponds to a mesh, and false otherwise  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_mesh_detect.m)
  """

  return _Runtime.call("spm_mesh_detect", *args, **kwargs)
