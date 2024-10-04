from spm.__wrap__ import _Runtime


def _surface_shift(*args, **kwargs):
  """  SURFACE_SHIFT inflates or deflates a triangulated surface by moving the  
    vertices outward or inward along their normals.  
     
    Use as  
      pos = surface_inflate(pos, tri, amount)  
    where pos and tri describe the surface.  
     
    See also SURFACE_NORMALS, SURFACE_ORIENTATION, SURFACE_INSIDE,  
    SURFACE_NESTING  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/surface_shift.m)
  """

  return _Runtime.call("surface_shift", *args, **kwargs)
