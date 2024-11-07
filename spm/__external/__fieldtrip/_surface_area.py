from spm.__wrapper__ import Runtime


def _surface_area(*args, **kwargs):
    """
      SURFACE_AREA computes the surface area of each of the triangles in a mesh  
         
        Use as  
          area = surface_area(pos, tri)  
         
        See also SURFACE_ORIENTATION, SURFACE_INSIDE, SURFACE_NESTING, PROJECTTRI, PCNORMALS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/surface_area.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("surface_area", *args, **kwargs)
