from spm.__wrap__ import _Runtime


def _find_outermost_boundary(*args, **kwargs):
  """  FIND_OUTERMOST_BOUNDARY locates outermost compartment of a BEM model  
    by looking at the containment of the triangular meshes describing   
    the surface boundaries  
     
    [outermost] = find_innermost_boundary(bnd)  
     
    with the boundaries described by a struct-array bnd with  
      bnd(i).pnt  vertices of boundary i (matrix of size Nx3)  
      bnd(i).tri  triangles of boundary i (matrix of size Mx3)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/find_outermost_boundary.m)
  """

  return _Runtime.call("find_outermost_boundary", *args, **kwargs)
