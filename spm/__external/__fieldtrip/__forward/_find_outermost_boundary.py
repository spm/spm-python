from spm._runtime import Runtime


def _find_outermost_boundary(*args, **kwargs):
    r"""
      FIND_OUTERMOST_BOUNDARY locates outermost compartment of a BEM model  
        by looking at the containment of the triangular meshes describing   
        the surface boundaries  
         
        [outermost] = find_innermost_boundary(bnd)  
         
        with the boundaries described by a struct-array bnd with  
          bnd(i).pnt  vertices of boundary i (matrix of size Nx3)  
          bnd(i).tri  triangles of boundary i (matrix of size Mx3)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/forward/private/find_outermost_boundary.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("find_outermost_boundary", *args, **kwargs)
