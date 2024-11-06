from spm.__wrapper__ import Runtime


def _find_innermost_boundary(*args, **kwargs):
    """
      FIND_INNERMOST_BOUNDARY locates innermost compartment of a BEM model  
        by looking at the containment of the triangular meshes describing   
        the surface boundaries  
         
        [innermost] = find_innermost_boundary(bnd)  
         
        with the boundaries described by a struct-array bnd with  
          bnd(i).pnt  vertices of boundary i (matrix of size Nx3)  
          bnd(i).tri  triangles of boundary i (matrix of size Mx3)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/inverse/private/find_innermost_boundary.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("find_innermost_boundary", *args, **kwargs)
