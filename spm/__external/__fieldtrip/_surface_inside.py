from spm.__wrapper__ import Runtime


def _surface_inside(*args, **kwargs):
    """
      SURFACE_INSIDE determines if a point is inside/outside a triangle mesh  
        whereby the bounding triangle mesh should be closed.  
         
        Use as  
          inside = surface_inside(dippos, pos, tri)  
        where  
          dippos  position of point of interest (can be 1x3 or Nx3)  
          pos     bounding mesh vertices  
          tri     bounding mesh triangles  
         
        See also SURFACE_AREA, SURFACE_ORIENTATION, SURFACE_NORMALS, SURFACE_NESTING, SOLID_ANGLE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/surface_inside.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("surface_inside", *args, **kwargs)
