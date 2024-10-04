from spm.__wrap__ import _Runtime


def _surface_normals(*args, **kwargs):
  """  SURFACE_NORMALS compute the surface normals of a triangular mesh  
    for each triangle or for each vertex  
     
    Use as  
      nrm = surface_normals(pnt, tri, opt)  
    where opt is either 'vertex' (default) or 'triangle'.  
     
    See also SURFACE_ORIENTATION, SURFACE_INSIDE, SURFACE_NESTING, PROJECTTRI, PCNORMALS  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/surface_normals.m)
  """

  return _Runtime.call("surface_normals", *args, **kwargs)
