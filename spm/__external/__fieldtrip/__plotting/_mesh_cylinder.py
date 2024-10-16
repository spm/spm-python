from spm.__wrapper__ import Runtime


def _mesh_cylinder(*args, **kwargs):
  """  MESH_CYLINDER creates a triangulated cylinder  
     
    Use as  
      [pnt, tri] = mesh_cylinder(Naz, Nel)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/mesh_cylinder.m)
  """

  return Runtime.call("mesh_cylinder", *args, **kwargs)
