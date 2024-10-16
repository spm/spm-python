from spm.__wrapper__ import Runtime


def _mesh_cube(*args, **kwargs):
  """  MESH_CUBE creates a triangulated cube  
     
    Use as  
      [pos, tri] = mesh_cube()  
     
    See also MESH_TETRAHEDRON, MESH_OCTAHEDRON, MESH_ICOSAHEDRON, MESH_SPHERE, MESH_CONE  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/mesh_cube.m)
  """

  return Runtime.call("mesh_cube", *args, **kwargs)
