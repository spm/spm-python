from spm.__wrap__ import _Runtime


def _mesh_icosahedron(*args, **kwargs):
  """  MESH_ICOSAHEDRON returns the vertices and triangle of a 12-vertex icosahedral  
    mesh.  
     
    Use as  
      [pos, tri] = mesh_icosahedron  
     
    See also MESH_TETRAHEDRON, MESH_OCTAHEDRON, MESH_SPHERE  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/mesh_icosahedron.m)
  """

  return _Runtime.call("mesh_icosahedron", *args, **kwargs)
