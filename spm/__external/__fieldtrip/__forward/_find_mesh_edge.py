from spm.__wrapper__ import Runtime


def _find_mesh_edge(*args, **kwargs):
  """  FIND_MESH_EDGE returns the edge of a triangulated mesh  
     
    [pnt, line] = find_mesh_edge(pnt, tri), where  
     
    pnt   contains the vertex locations and   
    line  contains the indices of the linepieces connecting the vertices  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/find_mesh_edge.m)
  """

  return Runtime.call("find_mesh_edge", *args, **kwargs)
