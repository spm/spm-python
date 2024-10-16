from spm.__wrapper__ import Runtime


def _mesh2edge(*args, **kwargs):
  """  MESH2EDGE finds the edge lines from a triangulated mesh or the edge  
    surfaces from a tetrahedral or hexahedral mesh. An edge is defined as an  
    element that does not border any other element. This also implies that a  
    closed triangulated surface has no edges.  
     
    Use as  
      [edge] = mesh2edge(mesh)  
     
    See also POLY2TRI  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/mesh2edge.m)
  """

  return Runtime.call("mesh2edge", *args, **kwargs)
