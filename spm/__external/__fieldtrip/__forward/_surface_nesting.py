from spm.__wrapper__ import Runtime


def _surface_nesting(*args, **kwargs):
    """
      SURFACE_NESTING determines what the order of multiple boundaries is to  
        get them sorted with the innermost or outermost surface first.  
         
        Use as  
          order = surface_nesting(bnd, desired)  
        where bnd is a structure-array with multiple closed and nested meshes.  
         
        Note that it does not check for intersections and may fail for  
        intersecting surfaces.  
         
        See also SURFACE_ORIENTATION, SURFACE_NORMALS, SURFACE_INSIDE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/surface_nesting.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("surface_nesting", *args, **kwargs)
