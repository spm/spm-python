from spm.__wrapper__ import Runtime


def _find_vertex_neighbours(*args, **kwargs):
  """  FIND_VERTEX_NEIGHBOURS determines the neighbours of a specified vertex  
    in a mesh.  
      
    [nb] = find_vertex_neighbours(pnt, tri, indx)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/find_vertex_neighbours.m)
  """

  return Runtime.call("find_vertex_neighbours", *args, **kwargs)
