from spm.__wrapper__ import Runtime


def _projecttri(*args, **kwargs):
  """  PROJECTTRI makes a closed triangulation of a list of vertices by  
    projecting them onto a unit sphere and subsequently by constructing  
    a convex hull triangulation.  
     
    Use as  
      tri = projecttri(pos, method)  
    where method is either 'convhull' (default) or 'delaunay'.  
     
    See also SURFACE_NORMALS, PCNORMALS, ELPROJ  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/projecttri.m)
  """

  return Runtime.call("projecttri", *args, **kwargs)
