from spm.__wrap__ import _Runtime


def _intersect_plane(*args, **kwargs):
  """  INTERSECT_PLANE intersection between a triangulated surface mesh and a plane. It  
    returns the coordinates of the begin- and endpoints of the line segments that  
    together form the contour of the intersection.  
     
    Use as  
      [X, Y, Z] = intersect_plane(pos, tri, v1, v2, v3)  
     
    where the intersecting plane is spanned by the vertices v1, v2, v3 and the return  
    values are the X, Y and Z coordinates of the begin- and endpoints for all line  
    segments.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/intersect_plane.m)
  """

  return _Runtime.call("intersect_plane", *args, **kwargs)
