from spm.__wrapper__ import Runtime


def _surface_orientation(*args, **kwargs):
  """  SURFACE_ORIENTATION returns the string 'inward' or 'outward' or 'unknown',  
    depending on the surface orientation.  
     
    Use as  
      str = surface_orientation(pos, tri)  
    or  
      str = surface_orientation(pos, tri, ori)  
     
    See also SURFACE_NESTING, SURFACE_NORMALS, SURFACE_NESTING  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/surface_orientation.m)
  """

  return Runtime.call("surface_orientation", *args, **kwargs)
