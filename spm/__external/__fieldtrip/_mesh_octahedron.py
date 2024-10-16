from spm.__wrapper__ import Runtime


def _mesh_octahedron(*args, **kwargs):
  """  MESH_OCTAHEDRON returns the vertices and triangles of an octahedron  
     
    Use as  
      [pos tri] = mesh_octahedron;  
     
    See also MESH_TETRAHEDRON, MESH_OCTAHEDRON, MESH_SPHERE  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/mesh_octahedron.m)
  """

  return Runtime.call("mesh_octahedron", *args, **kwargs)
