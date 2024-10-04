from spm.__wrap__ import _Runtime


def _tetrahedron(*args, **kwargs):
  """  TETRAHEDRON returns the vertices and triangles of a tetraedron  
     
    Use as  
      [pos, tri] = tetrahedron;  
     
    See also ICOSAHEDRON, OCTAHEDRON  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/tetrahedron.m)
  """

  return _Runtime.call("tetrahedron", *args, **kwargs)
