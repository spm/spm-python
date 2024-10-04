from spm.__wrap__ import _Runtime


def _remove_double_vertices(*args, **kwargs):
  """  REMOVE_DOUBLE_VERTICES removes double vertices from a triangular, tetrahedral or  
    hexahedral mesh, renumbering the vertex-indices for the elements.  
     
    Use as  
      [pos, tri] = remove_double_vertices(pos, tri)  
      [pos, tet] = remove_double_vertices(pos, tet)  
      [pos, hex] = remove_double_vertices(pos, hex)  
     
    See also REMOVE_VERTICES  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/remove_double_vertices.m)
  """

  return _Runtime.call("remove_double_vertices", *args, **kwargs)
