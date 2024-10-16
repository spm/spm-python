from spm.__wrapper__ import Runtime


def _poly2tri(*args, **kwargs):
  """  POLY2TRI converts the polygons in a mesh to triangles by splitting  
    them in half. The input polygons should consist of 4 vertices.  
    Curvature is not considered and the resulting split will only be  
    optimal for flat polygons.  
     
    Use as  
     mesh = poly2tri(mesh)  
     
    See also MESH2EDGE  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/poly2tri.m)
  """

  return Runtime.call("poly2tri", *args, **kwargs)
